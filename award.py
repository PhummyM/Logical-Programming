#A program that determines the award a person competing in a triathlon
#will receive.
#The program should accept user inputs for the times (in minutes) of all three
#triathlon events, namely swimming, cycling, and running, and then calculate and
#output the total time to complete the triathlon.

#Ask the user to enter the times for swimming, cycling, and running
swimming_time = float(input("Enter the time (in minutes) for swimming: "))
cycling_time = float(input("Enter the time (in minutes) for cycling: "))
running_time = float(input("Enter the time (in minutes) for running: "))

#Calculate the total time to complete the triathlon
total_time = swimming_time + cycling_time + running_time
#Print the total time
print(f"The total time to complete the triathlon is: {total_time} minutes")

#Determine the award based on the total time
if total_time <= 100:
    print("Within the qualifying time. 0-100 minutes")
    print("Award: Provincial Colours")
elif 100 < total_time <= 105:
    print("Within the qualifying time. 101-105 minutes")
    print("Award: Provincial Half Colours")
elif 105 < total_time <= 110:
    print("Within the qualifying time. 106-110 minutes")
    print("Award: Provincial Scroll")
else:
    print("Sorry, you did not win an award.")
    print("Award: No award")

