name = input("Enter your name: ").capitalize()
gender = input("Select your gender:\n1. Male\n2. Female: ")
print("Hey, " + name + "!")

choice = input("What do you want to find out? (BMI / BMR): ").upper()
age = int(input("What is your age? : "))
weight = float(input("What is your weight (in kg)? : "))
height = float(input("What is your height (in cm)? : "))

if choice == "BMR":
    def bmr():
        if gender == "1":
            result = 655 + (9.6 * weight) + (1.8 * height) - (4.7 * age)
            print(f"Dear {name}, Your BMR is {result} calories.")

        elif gender == "2":
            result = 655 + (9.6 * weight) + (1.8 * height) - (4.7 * age)
            print(f"Dear {name}, Your BMR is {result} calories.")

        else:
            print("Please enter the gender selection correctly!")

        def sug(result):
            print("Select your activity level:")
            print("A. Sedentary (little or no exercise)")
            print("B. Lightly active (light exercise/sports 1-3 days a week)")
            print("C. Moderately active (moderate exercise/sports 3-5 days a week)")
            print("D. Very active (hard exercise/sports 6-7 days a week)")
            print("E. Extra active (very hard exercise/sports and physical job or 2x training)")
            hc = input("Enter your choice here: ").upper()

            if hc == "A":
                do = result * 1.2
                print(f"{name}, you need around {do} calories per day.")

            elif hc == "B":
                do = result * 1.375
                print(f"{name}, you need around {do} calories per day.")

            elif hc == "C":
                do = result * 1.55
                print(f"{name}, you need around {do} calories per day.")

            elif hc == "D":
                do = result * 1.725
                print(f"{name}, you need around {do} calories per day.")

            elif hc == "E":
                do = result * 1.9
                print(f"{name}, you need around {do} calories per day.")

            else:
                print("Invalid input.")

        sug(result)

    bmr()


elif choice == "BMI":
    i_result = weight / ((height / 100) ** 2)
    print(f"Your BMI result is {i_result}.")

    if i_result < 18.5:
        print(f"{name}! You are underweight! You need to gain weight by eating in moderation.")

    elif 18.5 <= i_result <= 24.9:
        print(f"Congratulations, {name}! You are in the ideal standard of good health.")

    elif 25 <= i_result <= 29.9:
        print(f"{name}, you have excess body weight. You need to exercise regularly to lose the excess weight.")

    elif 30 <= i_result <= 34.9:
        print(f"{name}, you are in the first stage of obesity. You need a selective diet and exercise.")

    elif 35 <= i_result <= 39.9:
        print(f"{name}, you are in the second stage of obesity. You need a moderate diet and exercise.")

    elif i_result >= 40:
        print(f"{name}! You have excess weight. You are currently at risk. Consult a doctor as soon as possible.")

    else:
        print("Invalid input.")

else:
    print("Please select BMI/BMR accurately.")
