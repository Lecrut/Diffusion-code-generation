import sys

def compare_values(value1, value2):
    if value1 > value2:
        return 'Value A is larger'
    else:
        return 'Value B is larger'
if __name__ == '__main__':
    value_a = 42
    value_b = 27
    result = compare_values(value_a, value_b)
    print(result)