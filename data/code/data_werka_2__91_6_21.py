from typing import Union

def negate_boolean(value: Union[bool, int]) -> bool:
    if isinstance(value, bool):
        logical_value = value
    elif isinstance(value, int):
        logical_value = bool(value)
    else:
        raise ValueError(f"Unsupported type: {type(value).__name__}")
    
    is_true = logical_value is True
    negated = not is_true
    return negated

if __name__ == '__main__':
    sample_input_1 = 1
    sample_input_2 = 0
    
    result_1 = negate_boolean(sample_input_1)
    result_2 = negate_boolean(sample_input_2)
    
    print(result_1)
    print(result_2)