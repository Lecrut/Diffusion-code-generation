def check_number(number):
    if number > 0:
        print("Positive")
    elif number < 0:
        print("Negative")
    else:
        print("Zero")
if __name__ == '__main__':
    test_numbers = [10, -5, 0, 3.14, -100]
    for num in test_numbers:
        check_number(num)