def is_odd(number):
    return number % 2 == 1

if __name__ == '__main__':
    sample_values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    for value in sample_values:
        print(f"{value} is odd: {is_odd(value)}")