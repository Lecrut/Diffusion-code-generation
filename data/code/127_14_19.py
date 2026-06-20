def is_odd(n):
    return n & 1

if __name__ == '__main__':
    sample_values = [4, 5, 6, 7]
    for value in sample_values:
        print(f"Is {value} odd? {is_odd(value)}")