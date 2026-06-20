def check_negative(value):
    return value < 0

if __name__ == '__main__':
    sample_values = [5, -3, 2, -1]
    for value in sample_values:
        if check_negative(value):
            print(f"{value} is negative.")
        else:
            print(f"{value} is not negative.")