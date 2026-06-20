def verify_oddity(number):
    return number % 2 != 0

if __name__ == '__main__':
    num1 = 7
    num2 = 8
    num3 = 9
    print(f"Number {num1} is odd: {verify_oddity(num1)}")
    print(f"Number {num2} is odd: {verify_oddity(num2)}")
    print(f"Number {num3} is odd: {verify_oddity(num3)}")