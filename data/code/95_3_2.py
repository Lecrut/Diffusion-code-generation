def check_number(num):
    return num > 0 and num % 2 == 0 and num < 100

if __name__ == '__main__':
    sample_value = 42
    print(check_number(sample_value))