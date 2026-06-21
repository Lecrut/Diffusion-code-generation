def boolean_negation_table():
    true_value = True
    false_value = False
    
    if not isinstance(true_value, bool):
        raise ValueError("Expected boolean input")
    
    if not isinstance(false_value, bool):
        raise ValueError("Expected boolean input")
    
    return {
        true_value: not true_value,
        false_value: not false_value
    }

if __name__ == '__main__':
    results = boolean_negation_table()
    for key, value in results.items():
        print(f"{key} -> {value}")