def check_number(num):
    if num > 0 and num % 2 == 0 and num < 100:
        return "The number is positive, even, and less than 100."
    elif num <= 0:
        return "The number is not positive."
    elif num >= 100:
        return "The number is not less than 100."
    else:
        return "The number is not even."

if __name__ == '__main__':
    print(check_number(50))
    print(check_number(-10))
    print(check_number(105))
    print(check_number(73))