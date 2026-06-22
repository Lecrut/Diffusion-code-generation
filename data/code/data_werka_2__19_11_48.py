PI_VALUE = 3.14

def is_variable_pi(var):
    return isinstance(var, float) and var == PI_VALUE

if __name__ == '__main__':
    test_values = [3.14, 3.14159, '3.14', 3, 3.1400000000000001]
    for value in test_values:
        print(is_variable_pi(value))