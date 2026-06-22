def is_strictly_less_than_zero(num):
    return num < 0

if __name__ == '__main__':
    sample_values = [-1.0, -0.0, 0.0, 1.0]
    for value in sample_values:
        print(is_strictly_less_than_zero(value))