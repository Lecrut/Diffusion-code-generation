def is_valid_number(num):
    return num > 0 and num % 2 == 0 and num < 100

if __name__ == '__main__':
    sample_value = 64
    if is_valid_number(sample_value):
        print("All conditions met")
    else:
        print("One or more conditions failed")