def negate_boolean(boolean_value):
    if not isinstance(boolean_value, bool):
        raise ValueError("Input must be a boolean value")
    
    return not boolean_value

if __name__ == '__main__':
    sample_values = [True, False]
    for value in sample_values:
        print(f"Original value: {value}, Negated value: {negate_boolean(value)}")