import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("hypothetical_logistics_dataset.csv")
print(df.describe())
print(df[["Distance_km","Volume_Units","Actual_Delivery_Days","Transport_Cost_INR"]].corr())

plt.hist(df["Actual_Delivery_Days"], bins=30)
plt.xlabel("Actual Delivery Days")
plt.ylabel("Shipments")
plt.title("Distribution of Actual Delivery Time")
plt.show()

df.groupby("Region")["Transport_Cost_INR"].mean().plot(kind="bar")
plt.ylabel("Average Transport Cost (INR)")
plt.title("Average Transport Cost by Region")
plt.show()

plt.scatter(df["Distance_km"],df["Transport_Cost_INR"],alpha=.35)
plt.xlabel("Distance (km)")
plt.ylabel("Transport Cost (INR)")
plt.title("Distance vs Transport Cost")
plt.show()
