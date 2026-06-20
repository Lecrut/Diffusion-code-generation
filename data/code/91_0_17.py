def negate_boolean(boolean_value):
    if not isinstance(boolean_value, bool):
        raise ValueError("Input must be a boolean")
    
    return not boolean_value

if __name__ == '__main__':
    sample_value = True
    print(f"Negation of {sample_value}: {negate_boolean(sample_value)}")