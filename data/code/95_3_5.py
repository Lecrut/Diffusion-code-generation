def check_number(num):
    return num > 0 and num % 2 == 0 and num < 100

if __name__ == '__main__':
    sample_values = [50, -10, 99, 101]
    for value in sample_values:
        print(f"{value}: {check_number(value)}")