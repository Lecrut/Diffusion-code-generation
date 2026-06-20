def verify_oddity(num):
    return num % 2 != 0

if __name__ == '__main__':
    number1 = 7
    number2 = 10
    print(f"Number {number1} is odd: {verify_oddity(number1)}")
    print(f"Number {number2} is odd: {verify_oddity(number2)}")