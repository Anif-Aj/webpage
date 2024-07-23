import streamlit as st

# Add some text to our app
st.title("My Awesome Streamlit App")
st.write("Pick a number, a date, and your favorite pet!")

# Let's add a slider for picking a number
number = st.slider("Pick a number", 0, 100)

# And a date picker
date = st.date_input("Pick a date")

# Now, let's give them pet options
pets = ["Dog", "Cat", "Bird"]
pet = st.radio("Pick a pet", pets)

# Display their choices
st.write(f"You picked: Number {number}, Date {date}, and Pet: {pet}")

# And why not add a chart?
my_chart = st.line_chart({"data": [20, 40, 60, 80, 100]})

#That's our simple Streamlit app.
