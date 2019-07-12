def deadlift():
    one_max = (int(weight)) * 1.09 + 14.25
    if kilos_or_pounds == "Kilos":
        print("Your one rep max is " + str(one_max) + " kilograms.")
    elif kilos_or_pounds == "Pounds":
        print("Your one rep max is " + str(one_max * 2.20) + " pounds.")


def squat():
    one_max = (int(weight)) * 1.09 + 14.25
    if kilos_or_pounds == "Kilos":
        print("Your one rep max is " + str(one_max) + " kilograms.")
    elif kilos_or_pounds == "Pounds":
        print("Your one rep max is " + str(one_max * 2.20) + " pounds.")


def bench_press():
    one_max = (int(weight)) * 1.13 + 0.69
    if kilos_or_pounds == "Kilos":
        print("Your one rep max is " + str(one_max) + " kilograms.")
    elif kilos_or_pounds == "Pounds":
        print("Your one rep max is " + str(one_max * 2.20) + " pounds.")


def overheadpress():
    one_max = (int(weight)) * 1.13 + 0.69
    if kilos_or_pounds == "Kilos":
        print("Your one rep max is " + str(one_max) + " kilograms.")
    elif kilos_or_pounds == "Pounds":
        print("Your one rep max is " + str(one_max * 2.20) + " pounds.")


print("""\n Welcome to the 1RM calculator. Which exercise would you like to 
        calculate? You can choose: """)

exercises = ['Squat', 'Deadlift', 'Bench Press', 'Overhead Press']
print('\n'.join(map(str, exercises)))

exercise = input("Which would you like to choose? ").title()
kilos_or_pounds = input("Would you like your answer to be in kilos or pounds? ").title()
weight = int(input("What weight can you rep for 4-6 reps in that compound? "))

if str(exercise) == "Deadlift":
    deadlift()
elif str(exercise) == "Bench Press":
    bench_press()

elif str(exercise) == "Squat":
    squat()

elif str(exercise) == "Overhead Press":
    overheadpress()


