def validate_and_operation(sequence):
    if not all(char in '01' for char in sequence):
        raise ValueError("Input must be a string of '1's and '0's.")
    
    return all(char == '1' for char in sequence)

if __name__ == '__main__':
    test_cases = [
        "111",
        "000",
        "101",
        "110",
        "010"
    ]
    
    results = [validate_and_operation(case) for case in test_cases]
    print(results)