def validate_variable(var):
    return isinstance(var, float)

def is_value_pi(value):
    return value == 3.14

def check_variable(var):
    if not validate_variable(var):
        return False
    return is_value_pi(var)

if __name__ == '__main__':
    sample_values = [3.14, 3.14159, '3.14', 3, 3.1400000000000001]
    for value in sample_values:
        print(check_variable(value))