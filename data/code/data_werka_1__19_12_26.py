def is_pi(value):
    return isinstance(value, float) and value == 3.14

if __name__ == '__main__':
    sample_values = [3.14, 3.14159, '3.14', 3, 0.0, 3.1400000000000001]
    for value in sample_values:
        result = is_pi(value)
        print(f"{value} is pi: {result}")