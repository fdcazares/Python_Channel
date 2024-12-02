# -*- coding: UTF-8 -*-
"""PyBank Homework Starter File."""

# Dependencies
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("/Users/freddycazares/Documents/Boot Camp/Homework/Python Challenge/Starter_Code/PyBank/Resources/budget_data.csv")  # Input file path
file_to_output = os.path.join("/Users/freddycazares/Documents/Boot Camp/Homework/Python Challenge/Starter_Code/PyBank/analysis", "budget_analysis.txt")  # Output file path

# Define variables to track the financial data
total_months = 0
month_of_change = []
net_change_list = []
greatest_increase = ["",0]
greatest_decrease = ["",99999999999999999999999999999]
total_net = 0
# Add more variables to track other necessary financial data

# Open and read the csv
with open(file_to_load) as financial_data:
    reader = csv.reader(financial_data)

    # Skip the header row
    header = next(reader)

    # Extract first row to avoid appending to net_change_list
    first_row = next(reader)
    total_months += 1
    total_net += int(first_row[1])
    prev_net = int(first_row[1])


    # Track the total and net change


    # Process each row of data
    for row in reader:

        # Track the total
        total_months += 1
        total_net += int(first_row[1])


        # Track the net change
        net_change = int(row[1]) - prev_net
        # This is to set up the dictionaries for the next loop
        prev_net = int(row[1])
        net_change_list += [net_change]
        month_of_change += [row[0]]


        # Calculate the greatest increase in profits (month and amount)
        if net_change > greatest_increase[1]:
            greatest_increase[0] = row[0] #replaces whichever value for netchange is greater than the original value of greatest_increase which was set to 0, first column is just the month
            greatest_increase[1] = net_change #same thing but replaces 0 with the new greatest net_change.

        # Calculate the greatest decrease in losses (month and amount)
        if net_change < greatest_decrease[1]:
            greatest_decrease[0] = row[0]
            greatest_decrease[1] = net_change


# Calculate the average net change across the months
net_monthly_avg = sum(net_change_list)/len(net_change_list)

# Generate the output summary
output = (
    f"Financial Analysis\n"
    f"Total Months: {total_months}\n"
    f"Total: ${total_net}\n"
    f"Average Change: {net_monthly_avg}\n"
    f"Greatest Increase in Profit: {greatest_increase[0]}(${greatest_increase[1]})\n"
    f"Greatest Decrease in Profit: {greatest_decrease[0]}(${greatest_decrease[1]})\n"

)

# Print the output
print(output)

# Write the results to a text file
with open(file_to_output, "w") as txt_file:
    txt_file.write(output)
