import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv(r"C:\Users\user\Desktop\Student_Perfomance_Analyzer\dataset\student_data.csv")

print(data)
print("\nDataset Information:")
print(data.info())

print("\nStatistical Summary:")
print(data.describe())
def classify_performance(marks):
    if marks >= 85:
        return "Excellent"
    elif marks >= 70:
        return "Good"
    elif marks >= 50:
        return "Average"
    else:
        return "Poor"


data["Performance"] = data["Final_Marks"].apply(classify_performance)

print("\nStudent Performance:")
print(data[["Student_ID", "Final_Marks", "Performance"]])
average_marks = data["Final_Marks"].mean()
highest_marks = data["Final_Marks"].max()
lowest_marks = data["Final_Marks"].min()

passed_students = (data["Final_Marks"] >= 50).sum()
pass_percentage = (passed_students / len(data)) * 100

print("\nOverall Performance:")
print("Average Final Marks:", average_marks)
print("Highest Final Marks:", highest_marks)
print("Lowest Final Marks:", lowest_marks)
print("Passed Students:", passed_students)
print("Pass Percentage:", pass_percentage, "%")
plt.bar(data["Student_ID"], data["Final_Marks"])

plt.xlabel("Student ID")
plt.ylabel("Final Marks")
plt.title("Student Final Marks")

plt.show()
plt.scatter(data["Attendance"], data["Final_Marks"])

plt.xlabel("Attendance")
plt.ylabel("Final Marks")
plt.title("Attendance vs Final Marks")

plt.show()
performance_count = data["Performance"].value_counts()

print("\nPerformance Distribution:")
print(performance_count)
plt.pie(performance_count, labels=performance_count.index, autopct="%1.1f%%")
plt.title("Student Performance Distribution")
plt.show()
print("\nCorrelation Analysis:")
correlation = data[["Attendance", "Study_Hours", "Assignment_Score", "Internal_Marks", "Final_Marks"]].corr()
print(correlation)