MIN_VALUE = 0
MAX_VALUE = 100

def is_valid_number(num):
    return num > MIN_VALUE and num % 2 == 0 and num < MAX_VALUE

if __name__ == '__main__':
    sample_values = [50, -10, 100, 3.14]
    for value in sample_values:
        print(f"{value}: {is_valid_number(value)}")