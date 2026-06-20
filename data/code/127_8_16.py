def is_odd(number):
    return number & 1 == 1

if __name__ == '__main__':
    test_values = [2, 3, 4, 5, 6]
    for value in test_values:
        print(f"Number: {value}, Is Odd: {is_odd(value)}")