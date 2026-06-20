def compare_booleans(a: bool, b: bool) -> bool:
    if not isinstance(a, bool) or not isinstance(b, bool):
        raise ValueError("Both inputs must be boolean values")
    return a == b

if __name__ == '__main__':
    sample_inputs = [
        (True, True),
        (False, False),
        (True, False)
    ]
    
    for inputs in sample_inputs:
        result = compare_booleans(*inputs)
        print(f"compare_booleans{inputs} -> {result}")