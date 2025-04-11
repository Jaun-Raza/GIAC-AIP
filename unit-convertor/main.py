import streamlit as st

st.title("Unit Convertor")
st.markdown("### Converts Length, Weight by this convertor")
st.write(" Select a category, enter a value and get the converted result in real-time")

category = st.selectbox(" Choose a category", ["Length", "Weight"])

def converts_units(category, value, unit):
    if category == "Length":
        if unit == "Kilometers to Miles":
            return value * 0.621371
        elif unit == "Miles to Kilometers":
            return value / 0.621371

    elif category == "Weight": 
        if unit == "Kilograms to Grams":
            return value * 2.20462
        elif unit == "Grams to Kilograms":
            return value / 2.20462

    return 0

if category == "Length":
    unit = st.selectbox("Select Unit", ["Miles to Kilometers", "Kilometers to Miles"])
else:
    unit = st.selectbox("Select Unit", ["Kilograms to Grams", "Grams to Kilograms"])

value = st.number_input("Enter a value to convert")

if st.button("Convert"):
    result = converts_units(category, value, unit)
    st.success(f"The result of converstion is {result:.2f}")