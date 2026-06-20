def check_value(num):
    return num > 0 and num % 2 == 0 and num < 100

if __name__ == '__main__':
    sample_values = [50, -10, 100, 3.14]
    for value in sample_values:
        print(f"{value}: {check_value(value)}")