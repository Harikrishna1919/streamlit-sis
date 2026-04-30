# Import python packages.
import streamlit as st
from snowflake.snowpark.context import get_active_session
from snowflake.snowpark.functions import col

# Write directly to the app.
st.title(f"customize your smoothies :cup_with_straw:")
st.write(
  """choose fruits u want in custome smoothies
  """
)

name_on_order=st.text_input('name on smoothie:')
st.write('the name on the smoothies is:',name_on_order)

session = get_active_session()

my_dataframe = session.table("SMOOTHIES.PUBLIC.FRUIT_OPTIONS").select(col("FRUIT_NAME"))

st.dataframe(my_dataframe, use_container_width=True)
ingredients_list=st.multiselect(
'choose upto 5 ingredients:'
,my_dataframe,
max_selections=5)
if ingredients_list:
   

    ingredients_string=''

    for fruit_choosen in ingredients_list:
        ingredients_string+=fruit_choosen+' '
        
    #st.write(ingredients_string)
    my_insert_stmt = """insert into smoothies.public.orders1
    (ingredients, name_on_order)
    values ('""" + ingredients_string + """',
            '""" + name_on_order + """')"""
    st.write(my_insert_stmt)
    time_to_insert=st.button('submit order')
    if time_to_insert:
        session.sql(my_insert_stmt).collect()
        st.success('Your Smoothie is ordered!', icon="✅")
        






