def is_negative(value):
    return value < 0

if __name__ == '__main__':
    sample_value = -3
    if is_negative(sample_value):
        print(f"{sample_value} is negative.")
    else:
        print(f"{sample_value} is not negative.")