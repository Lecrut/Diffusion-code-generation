import random
if __name__ == '__main__':
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    if num1 == num2:
        print("The two entered values are equal.")
    else:
        print("The two entered values differ.")