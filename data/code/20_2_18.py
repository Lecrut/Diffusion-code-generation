def check_even(number):
    return number % 2 == 0

if __name__ == '__main__':
    sample_values = [0, 1, 2, 3, 4, -2, 100]
    for val in sample_values:
        result = check_even(val)
        print(f"{val}: {result}")