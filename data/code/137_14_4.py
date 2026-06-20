def check_number(number):
    if number & 1 == 0:
        return "Even"
    else:
        return "Odd"

if __name__ == '__main__':
    test_numbers = [10, -5, 0, 3.14, -100]
    for num in test_numbers:
        print(f"Number {num} is: {check_number(num)}")