def is_odd(num):
    return num % 2 != 0

if __name__ == '__main__':
    test_values = [10, 15, 20, 25]
    for value in test_values:
        print(f"{value} is odd: {is_odd(value)}")