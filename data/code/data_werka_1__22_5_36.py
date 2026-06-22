def is_odd(number):
    return number % 2 != 0

if __name__ == '__main__':
    sample_values = [4, 7, 10, 13]
    for value in sample_values:
        result = is_odd(value)
        print(f"{value} is odd: {result}")