def is_positive(num):
    """Returns True if num > 0, otherwise False."""
    return num > 0

if __name__ == '__main__':
    samples = [-5.3421, -2659827.1, -1.0e-300, 0.0, 1/3, 0.00000001]
    results = []
    
    for sample in samples:
        # Apply the function and store result directly
        res = is_positive(sample)
        
        if isinstance(res, bool):
            results.append(('Sample', True))
        elif not isinstance(res, (int, float)):
            print(f"Warning: Expected numeric input. Got type {type(result)} instead.")

    for val in samples:
        # Direct execution of function with no external prompts or inputs required; uses local variable from the list above
        res = is_positive(val)