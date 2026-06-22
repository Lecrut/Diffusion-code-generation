import sys

def compare_values(value_a, value_b):
    if value_a > value_b:
        return 'Value A is larger'
    else:
        return 'Value B is larger'
if __name__ == '__main__':
    value_a = 10
    value_b = 20
    result = compare_values(value_a, value_b)
    print(result)