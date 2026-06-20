def check_number(num):
    if num > 0 and num % 2 == 0 and num < 100:
        return "The number is positive, even, and less than 100."
    else:
        return "The number does not meet the criteria."

if __name__ == '__main__':
    print(check_number(42))
    print(check_number(99))
    print(check_number(100))
    print(check_number(-2))