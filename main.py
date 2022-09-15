# Assignment number 1
for num in range(1, 10001, 10):
    print(num)

# Assignment number 2
heights_list = [171, 154, 190, 168, 180, 189, 162, 155, 178, 175]

i = 0
count = 0
while i < 10:
    # I checked the output of this code by using a for loop, code:
    # for height in heights_list:
    # I called the variable in the for loop height, and removed the original height variable.

    height = int(input("enter your height: "))  # The code will crash if the input is a decimal enhancer
    i = i + 1
    if height < 170:
        print("no entrance for you, shorty! your height is ", height)
    else:
        count = count + 1
print(count)

# The output is:
#   no entrance for you, shorty! your height is 154
#   no entrance for you, shorty! your height is 168
#   no entrance for you, shorty! your height is 162
#   no entrance for you, shorty! your height is 155
#   6

# Assignment number 3
# The mistake in this code is that there is no weight variable or condition.
# possible solution:
i = 0
count = 0
while i < 10:
    while True:
        try:
            height = int(input("enter your height: "))
            weight = int(input("enter your weight: "))
        except ValueError:
            print("\nThe height and the weight must be an integer!")
        else:
            break
    i = i + 1
    if height < 170 and weight < 75 or weight > 100:
        print(f"no entrance for you! your height is {height}, your weight is {weight}\n")
    else:
        count = count + 1
print(count)

# optional assignment number 4
number_of_soldiers = 0
count_trees = 0
for soldier in range(1, 6):
    count_per_soldier = 0
    print(f"Soldier number {soldier}")
    for tree in range(1, 43):
        validate = False
        while validate is False:
            cut_check = input(f"Is tree number {tree} cut down? (Yes/ No): ").lower()
            if cut_check == "yes" or cut_check == "no":
                if tree % 3 == 0 and cut_check == "yes":
                    count_per_soldier += 1
                validate = True
            else:
                print("The answer you entered is invalid!\n")
    print("\n")
    if count_per_soldier >= 6:
        number_of_soldiers += 1
    count_trees += count_per_soldier

print(f"In total {count_trees} validate trees were cut down! "
      f"Monty Python has {number_of_soldiers} extraordinary soldiers!")
