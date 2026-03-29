import streamlit as st

st.title("AI Money Mentor 💰")

st.header("User Details")

salary = st.number_input("Enter your yearly salary (₹)", min_value=0)
age = st.number_input("Enter your age", min_value=18, max_value=100)

st.header("Tax Calculation")

if st.button("Calculate Tax"):

   
    if salary <= 250000:
        tax = 0
    elif salary <= 500000:
        tax = (salary - 250000) * 0.05
    elif salary <= 1000000:
        tax = (250000 * 0.05) + (salary - 500000) * 0.2
    else:
        tax = (250000 * 0.05) + (500000 * 0.2) + (salary - 1000000) * 0.3

    st.success(f"Estimated Tax: ₹{tax}")

  
    st.subheader("AI Suggestions")

    if salary < 500000:
        st.write("👉 Try to save at least 20% of your income")
        st.write("👉 Start small SIP investments (₹1000/month)")
    elif salary < 1000000:
        st.write("👉 Invest in mutual funds and emergency fund")
        st.write("👉 Save 30% of your income")
    else:
        st.write("👉 Diversify investments (stocks, MF, real estate)")
        st.write("👉 Focus on tax saving and wealth growth")

 
    st.subheader("Monthly Plan")

    monthly_income = salary / 12
    st.write(f"👉 Your monthly income: ₹{monthly_income}")

    savings = monthly_income * 0.3
    st.write(f"👉 Suggested monthly savings: ₹{savings}")
    st.write(f"👉 Suggested SIP investment: ₹{savings * 0.5}")

    st.subheader("Financial Goal Planning")

    goal = st.selectbox("Select your goal", ["House", "Car", "Retirement"])

    if goal == "House":
        st.write("👉 Save aggressively and invest in long-term funds")
    elif goal == "Car":
        st.write("👉 Plan for short-term savings and low-risk investments")
    else:
        st.write("👉 Focus on retirement funds and SIP investments")

   
    st.subheader("Advice")

    if salary > 1000000:
        st.write("👉 Invest in Mutual Funds and save tax using ELSS")
    elif salary > 500000:
        st.write("👉 Use 80C investments (PPF, LIC, ELSS)")
    else:
        st.write("👉 Start SIP early for wealth growth")

    
    st.subheader("Money Health Score")

    score = 0

    if savings > 10000:
        score += 40
    if salary > 500000:
        score += 30
    if age < 30:
        score += 30

    st.success(f"💯 Your Financial Health Score: {score}/100")

    
    st.warning("⚠️ This is AI-based guidance. Not a certified financial advice.")
st.header("Smart Financial Advice")

if st.button("Get Advice"):

    savings = salary * 0.2
    investment = salary * 0.3

    st.success(f"💰 Suggested Savings: ₹{savings}")
    st.success(f"📈 Suggested Investment: ₹{investment}")

    if age < 30:
        st.info("🚀 You are young! Invest more in stocks and mutual funds.")
    elif age < 50:
        st.warning("⚖️ Balance between stocks and safe investments.")
    else:
        st.error("🛡️ Focus on safe investments like FD and pension plans.")