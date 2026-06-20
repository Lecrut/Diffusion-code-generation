def check_number(x):
    return x > 0 and x % 2 == 0 and x < 100

if __name__ == '__main__':
    sample_value = 42
    print(check_number(sample_value))