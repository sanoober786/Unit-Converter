import streamlit as st

st.title("🌍😊Unit Converter App")
st.markdown("### Instantly Converts Between Length , Weight and Time Units")
st.write("Select Conversion Type")

        # Select Conversion Type

conversion_type = st.selectbox("Select Conversion Type", ["Length" , "Weight" , "Time"])

        # Define Unit Option

def convert_units(conversion_type, value , unit):
   
    if conversion_type == "Length":
        if unit == "Kilometers to miles":
            return value * 0.621371
        elif unit == "Miles to kilometers":
            return value / 0.621371
        
        elif conversion_type == "Weight":
            if unit == "Kilograms to pounds":
                return value * 2.20462
            elif unit == "Pounds to Kilograms":
                return value / 2.20462
           
            elif conversion_type == "Time":
                if unit == "Seconds to minutes":
                    return value /60
                elif unit == "Minutes to seconds":
                    return value * 60
                elif unit == "Minutes to hours":
                    return value / 60
                elif unit == "Hours to minutes":
                    return value * 60 
                elif unit == "Hours to days":
                    return value / 24
                elif unit == "Days to hours":
                    return value * 24
    return 0
        # Select Unit Based on Type

if conversion_type == "Length":
    unit = st.selectbox("📏Choose Conversation" ,["Kilometers to miles" , "Miles to kilometers"] )              
elif conversion_type == "Weight":
    unit = st.selectbox("⚖Choose Conversation" ,["Kilograms to pounds", "Pounds to Kilograms"] )
elif conversion_type == "Time":
    unit = st.selectbox("⏰Choose Conversation" ,["Seconds to minutes", "Minutes to seconds", "Minutes to hours", "Hours to minutes","Hours to days","Days to hours"] )
                
value = st.number_input("Enter your value")

      # Button to Calculate

if st.button("Convert Now"):
    result = convert_units(conversion_type, value, unit)
    st.success(f"✅**Result:**{value} ➡ {result:3f} 👍")