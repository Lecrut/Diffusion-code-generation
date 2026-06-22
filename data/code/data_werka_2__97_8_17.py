def compute_truth_table(input_a, input_b):
    if not isinstance(input_a, bool) or not isinstance(input_b, bool):
        raise ValueError("Inputs must be boolean values")
    
    operators = {
        "a": lambda: input_a,
        "b": lambda: input_b,
        "NOT a": lambda: not input_a,
        "NOT b": lambda: not input_b,
        "a AND b": lambda: input_a and input_b,
        "a OR b": lambda: input_a or input_b,
        "a XOR b": lambda: input_a ^ input_b,
        "a NAND b": lambda: not (input_a and input_b),
        "a NOR b": lambda: not (input_a or input_b),
        "a IMPLIES b": lambda: (not input_a) or input_b,
        "b IMPLIES a": lambda: (not input_b) or input_a,
    }
    
    return {key: func() for key, func in operators.items()}

if __name__ == '__main__':
    result = compute_truth_table(True, False)
    print(result)