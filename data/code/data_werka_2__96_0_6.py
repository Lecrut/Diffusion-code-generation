def _validate_boolean(value):
    if not isinstance(value, bool):
        raise ValueError(f"Expected boolean, got {type(value).__name__}")
    return value

def evaluate_nested_logic(a, b, c, d):
    validated_a = _validate_boolean(a)
    validated_b = _validate_boolean(b)
    validated_c = _validate_boolean(c)
    validated_d = _validate_boolean(d)
    
    left_clause = validated_a and validated_b
    right_clause = validated_c and (not validated_d)
    
    return left_clause or right_clause

if __name__ == '__main__':
    sample_a = True
    sample_b = False
    sample_c = True
    sample_d = False
    calculated_result = evaluate_nested_logic(sample_a, sample_b, sample_c, sample_d)
    print(calculated_result)