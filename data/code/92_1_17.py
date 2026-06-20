def validate_input(value):
    if not isinstance(value, bool):
        raise ValueError("Input must be a boolean value")

def find_opposite_truth(truth):
    validate_input(truth)
    return not truth

if __name__ == '__main__':
    sample1 = True
    result1 = find_opposite_truth(sample1)
    print(f"Opposite of {sample1} is {result1}")
    
    sample2 = False
    result2 = find_opposite_truth(sample2)
    print(f"Opposite of {sample2} is {result2}")