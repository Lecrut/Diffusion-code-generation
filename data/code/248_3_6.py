def sum_two_numbers(a, b):
    return a + b

if __name__ == '__main__':
    sample_values = {1: (3, 5), 2: (7, 9)}
    for key, values in sample_values.items():
        result = sum_two_numbers(*values)
        print(f"Result {key}: {result}")