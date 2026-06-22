def is_even(n):
    return n % 2 == 0

if __name__ == '__main__':
    sample_values = [10, 15, 22, 33, 40, -5, -8, -11]
    for value in sample_values:
        print(f"Is {value} even? {is_even(value)}")