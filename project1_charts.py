import pandas as pd
import matplotlib.pyplot as plt

# ----------------------------
# STEP 1: Create Sample Sales Data
# ----------------------------

data = {
    "Date": [
        "2024-01-05", "2024-01-15", "2024-02-10",
        "2024-02-20", "2024-03-05", "2024-03-18"
    ],
    "Category": [
        "Electronics", "Clothing", "Electronics",
        "Furniture", "Clothing", "Furniture"
    ],
    "Sales": [20000, 15000, 25000, 18000, 22000, 30000]
}

df = pd.DataFrame(data)

# Convert Date column to datetime
df["Date"] = pd.to_datetime(df["Date"])

print("Original Data:")
print(df)

# ----------------------------
# STEP 2: Line Chart (Sales Over Time)
# ----------------------------

plt.figure(figsize=(8,5))

plt.plot(df["Date"], df["Sales"], marker='o')

plt.title("Sales Over Time")
plt.xlabel("Date")
plt.ylabel("Sales Amount")

plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig("sales_over_time.png")
plt.show()

# ----------------------------
# STEP 3: Monthly Sales Aggregation
# ----------------------------

df["Month"] = df["Date"].dt.to_period("M")

monthly_sales = df.groupby("Month")["Sales"].sum()

print("\nMonthly Sales:")
print(monthly_sales)

plt.figure(figsize=(8,5))
monthly_sales.plot(kind="line", marker='o')

plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Total Sales")

plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig("monthly_sales.png")
plt.show()
