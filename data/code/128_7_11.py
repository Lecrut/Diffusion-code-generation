def is_negative(value):
    return value < 0

if __name__ == '__main__':
    sample_values = [-1, 0, 5]
    for val in sample_values:
        if is_negative(val):
            print(f"{val} is negative")
        else:
            print(f"{val} is not negative")