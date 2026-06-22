def is_odd(n):
    return n % 2 != 0

if __name__ == '__main__':
    sample_values = [10, 15, -7, 8, -3, 0]
    for value in sample_values:
        print(f"Is {value} odd? {is_odd(value)}")