def is_strictly_less_than_zero(number):
    return number < 0

if __name__ == '__main__':
    sample_values = [-1.0, -0.5, 0.0, 0.5, 1.0]
    for value in sample_values:
        result = is_strictly_less_than_zero(value)
        print(f"{value}: {result}")