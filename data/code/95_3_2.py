def check_value(n):
    return n > 0 and n % 2 == 0 and n < 100

if __name__ == '__main__':
    sample_values = [0, 2, 50, 100, -5]
    for val in sample_values:
        print(check_value(val))