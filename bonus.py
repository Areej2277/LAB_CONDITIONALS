weight = float(input("Please enter your weight (in kg):"))

height_cm = float(input("Please enter your height(in cm):"))


height = height_cm / 100
bmi = weight / (height ** 2)
print(f"Your BMI is: {bmi: .2f}")

if bmi >= 25:
    print("Your are overweight; you need to work out and watch your diet ")

elif bmi >= 18.5:
    print("Your are fit & healthe.")  

else:
    print("You are underweight. watch your health.")      