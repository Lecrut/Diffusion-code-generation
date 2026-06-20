ZERO = 0

def is_zero(value):
    return value == ZERO

if __name__ == '__main__':
    sample_values = [0, 5, -3, 0.0]
    for value in sample_values:
        result = is_zero(value)
        print(f"Value: {value}, Is Zero: {result}")