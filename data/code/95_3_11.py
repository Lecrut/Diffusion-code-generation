def is_valid_number(num):
    return num > 0 and num % 2 == 0 and num < 100

if __name__ == '__main__':
    sample_values = [34, -7, 99, 62]
    for value in sample_values:
        if is_valid_number(value):
            print(f"{value}: Valid")
        else:
            print(f"{value}: Invalid")