def check_even_odd(number):
    return number % 2 == 0

if __name__ == '__main__':
    test_values = [4, 7, 18, 23]
    for value in test_values:
        result = check_even_odd(value)
        print(f"Input: {value}, Is Even: {result}")