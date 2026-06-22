import sys

def compare_values(value_a, value_b):
    if value_a > value_b:
        return 'Value A is larger'
    else:
        return 'Value B is larger'
if __name__ == '__main__':
    value1 = 42
    value2 = 7
    result = compare_values(value1, value2)
    print(result)