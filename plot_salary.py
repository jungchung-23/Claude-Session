import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("toy_hr_data.csv")
salary = df["salary"]

mean_val = salary.mean()
median_val = salary.median()

fig, ax = plt.subplots(figsize=(9, 5))

ax.hist(salary, bins=15, color="steelblue", edgecolor="white", alpha=0.85)

ax.axvline(mean_val, color="red", linewidth=2, label=f"Mean: ${mean_val:,.0f}")
ax.axvline(median_val, color="blue", linewidth=2, linestyle="--", label=f"Median: ${median_val:,.0f}")

ax.text(mean_val, ax.get_ylim()[1] * 0.92, f"${mean_val:,.0f}", color="red",
        ha="center", va="bottom", fontsize=10, fontweight="bold")
ax.text(median_val, ax.get_ylim()[1] * 0.82, f"${median_val:,.0f}", color="blue",
        ha="center", va="bottom", fontsize=10, fontweight="bold")

ax.set_xlabel("Salary ($)", fontsize=12)
ax.set_ylabel("Count", fontsize=12)
ax.set_title("Distribution of Employee Salaries", fontsize=14)
ax.legend(fontsize=11)

plt.tight_layout()
plt.savefig("salary_distribution.png", dpi=150)
print(f"Mean: {mean_val:,.0f}  Median: {median_val:,.0f}")
