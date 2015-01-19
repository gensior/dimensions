from math import floor


print("Please enter the height to be converted.");
feet = int(input("First, enter the feet: "));
inches = int(input("Now, enter the inches: "));
total_inches = feet * 12 + inches;
cm = format(total_inches * 2.54, '.2f');

print("Your height is {} feet {} inches, or {} inches. That is {} cm."
    .format(floor(feet+ inches/12), inches % 12, total_inches, cm));

print("Please enter a second height to be converted.");
cm = int(input("Enter the height in centimeters: "));
inches = float(format(cm * 0.393701, '.3f'));
numerator = round(((inches % 12) % 1) * 8);

print("Your height is {} cm, or {} inches, or {} feet {}-{}/8 inches."
    .format(cm, inches, floor(inches/12), floor(inches % 12), numerator));
