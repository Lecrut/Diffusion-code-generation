def is_strictly_less_than_zero(number):
    return number < 0

if __name__ == '__main__':
    sample_values = [1.5, -2.3, 0.0, -0.0001, 100.0]
    for value in sample_values:
        result = is_strictly_less_than_zero(value)
        print(f"{value} < 0: {result}")