import sys

def compare_values(value1, value2):
    if value1 > value2:
        return 'Value A is larger'
    else:
        return 'Value B is larger'

if __name__ == '__main__':
    sample_value_a = 42
    sample_value_b = 30
    result = compare_values(sample_value_a, sample_value_b)
    print(result)