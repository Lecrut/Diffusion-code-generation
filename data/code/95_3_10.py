def check_number(n):
    return n > 0 and n % 2 == 0 and n < 100

if __name__ == '__main__':
    sample_value = 42
    print(check_number(sample_value))