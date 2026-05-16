import random
def main():
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    print(f"First number: {num1}")
    print(f"Second number: {num2}")
    addition_result = num1 + num2
    subtraction_result = num1 - num2
    print(f"Addition result: {num1} + {num2} = {addition_result}")
    print(f"Subtraction result: {num1} - {num2} = {subtraction_result}")
if __name__ == '__main__':
    main()