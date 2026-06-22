import sys

def compare_values(value1, value2):
    if value1 > value2:
        return 'Value A is larger'
    else:
        return 'Value B is larger'

if __name__ == '__main__':
    sample_value1 = 42
    sample_value2 = 7
    result = compare_values(sample_value1, sample_value2)
    print(result)