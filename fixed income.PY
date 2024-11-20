# Step 1: Import Libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Step 2: Bond Pricing Model
def bond_price(face_value, coupon_rate, periods, ytm):
    """
    Calculate the price of a bond.
    :param face_value: Face value of the bond
    :param coupon_rate: Annual coupon rate (as a decimal)
    :param periods: Number of periods until maturity
    :param ytm: Yield to maturity (as a decimal)
    :return: Bond price
    """
    coupon = face_value * coupon_rate
    discounted_coupons = sum([coupon / (1 + ytm)**t for t in range(1, periods + 1)])
    discounted_face_value = face_value / (1 + ytm)**periods
    return discounted_coupons + discounted_face_value

# Step 3: Yield Spread Analysis
def yield_spread(corporate_yield, treasury_yield):
    return corporate_yield - treasury_yield

# Step 4: Portfolio Optimization (Simple Allocation Example)
def optimize_bond_portfolio(bond_data):
    """
    Optimize bond allocations for risk-adjusted returns.
    :param bond_data: DataFrame with bond data (columns: ['Type', 'Yield', 'Risk'])
    :return: Optimal weights
    """
    bond_data['Adjusted Return'] = bond_data['Yield'] / bond_data['Risk']
    return bond_data['Adjusted Return'] / bond_data['Adjusted Return'].sum()

# Step 5: Daily Trade Report
def generate_trade_report(portfolio, market_data):
    """
    Generate a daily trade report summarizing portfolio performance and market changes.
    :param portfolio: DataFrame with current bond portfolio
    :param market_data: DataFrame with market yield data
    :return: Trade report
    """
    portfolio['Current Value'] = portfolio['Price'] * portfolio['Quantity']
    total_value = portfolio['Current Value'].sum()
    market_summary = market_data.describe()
    recommendations = market_data[market_data['Yield'] > market_data['Yield'].mean()]
    return total_value, market_summary, recommendations

# Step 6: Visualization
def plot_yield_curve(data):
    plt.figure(figsize=(10, 6))
    plt.plot(data['Maturity'], data['Yield'], marker='o', label="Yield Curve")
    plt.title("Yield Curve")
    plt.xlabel("Maturity (Years)")
    plt.ylabel("Yield (%)")
    plt.grid()
    plt.legend()
    plt.show()

# Step 7: Main Function
if __name__ == "__main__":
    # Example Bond Data
    bonds = pd.DataFrame({
        'Type': ['Government', 'Corporate', 'Municipal'],
        'Yield': [0.03, 0.05, 0.04],
        'Risk': [0.01, 0.02, 0.015],
        'Price': [100, 95, 97],
        'Quantity': [50, 30, 20]
    })
    
    # Market Yield Data
    market_data = pd.DataFrame({
        'Maturity': [1, 3, 5, 10, 20],
        'Yield': [0.02, 0.025, 0.03, 0.035, 0.04]
    })
    
    # Bond Pricing Simulation
    price = bond_price(face_value=1000, coupon_rate=0.05, periods=10, ytm=0.04)
    print("Simulated Bond Price:", round(price, 2))
    
    # Yield Spread Analysis
    spread = yield_spread(corporate_yield=0.05, treasury_yield=0.03)
    print("Yield Spread (Corporate vs Treasury):", spread)
    
    # Portfolio Optimization
    optimal_weights = optimize_bond_portfolio(bonds)
    print("Optimal Portfolio Weights:\n", optimal_weights)
    
    # Trade Report
    portfolio_value, market_summary, recommendations = generate_trade_report(bonds, market_data)
    print("Total Portfolio Value:", round(portfolio_value, 2))
    print("Market Summary:\n", market_summary)
    print("Trade Recommendations:\n", recommendations)
    
    # Yield Curve Visualization
    plot_yield_curve(market_data)
