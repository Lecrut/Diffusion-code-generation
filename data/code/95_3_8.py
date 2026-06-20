def is_valid_number(num):
    return num > 0 and num % 2 == 0 and num < 100

if __name__ == '__main__':
    test_values = [34, -5, 99, 101]
    for value in test_values:
        if is_valid_number(value):
            print(f"{value}: Valid")
        else:
            print(f"{value}: Invalid")