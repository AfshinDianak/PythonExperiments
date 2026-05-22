#This file is for practicing and learning scripting with python to become more efficient with DevOps
print("******This file is for practicing and learning scripting with python to become more efficient with DevOps*****")
age = 20
name ="Ed"
heigt = 190.0

x = 10
y = 5
sum = x + y
product = x * y

# print("Name: ", name)

# if age >= 25:
#     print(name, "you're allowed in.")
# else:
#     print("Too young")

# car_array = ["Cuppra", "Audi", "BMW", "BYD is rubish"]
# for car in car_array:
#     print(f"Current car: {car}")
numbers = [1,2,3,4,5,6]
for num in numbers:
    if num % 2 == 0:
        print(f"Skipping this even number: {num}")
        continue
    print(f"Current number:{num}")