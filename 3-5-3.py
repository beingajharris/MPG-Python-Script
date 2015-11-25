# Calculate the Miles Per Gallon
print("This program loves to calculate MPG!")
 
# Get miles driven from the user 
miles_driven = input("Please Enter the miles driven:")
# The next line Converts the text entered into a floating point number
miles_driven = float(miles_driven)
 
#Next is where we receive the gallons used from the user
gallons_used = input("Please Enter the gallons used:")
# And now we can proceed to convert the given text entered into a floating point number
gallons_used = float(gallons_used)
 
# Calculate and print the answer
mpg = miles_driven / gallons_used
print("Miles per gallon:", mpg)
