def is_zero(number):
    return number == 0

if __name__ == '__main__':
    sample_values = [0, 1, -1, 0.0, 1.0, -0.0]
    for value in sample_values:
        print(f"{value}: {is_zero(value)}")