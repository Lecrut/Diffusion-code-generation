def is_exactly_zero(number):
    return number == 0

if __name__ == '__main__':
    sample_values = [0, -0.0, 1e-308, 1, -1, 2.5]
    for value in sample_values:
        print(f"{value} is exactly zero: {is_exactly_zero(value)}")