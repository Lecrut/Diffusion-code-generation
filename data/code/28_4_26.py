import sys

def compare_values(value_a, value_b):
    if value_a > value_b:
        return 'Value A is larger'
    else:
        return 'Value B is larger'

if __name__ == '__main__':
    sample_value_a = 42
    sample_value_b = 27
    result = compare_values(sample_value_a, sample_value_b)
    print(result)