def validate_input(input_str):
    if not input_str.isdigit():
        raise ValueError("Input must be a string of '1's and '0's")
    if any(char not in '01' for char in input_str):
        raise ValueError("Input must contain only '1's and '0's")

def check_and_operation(sequence):
    validate_input(sequence)
    return all(int(bit) == 1 for bit in sequence)

if __name__ == '__main__':
    test_cases = [
        "000",
        "111",
        "011",
        "101",
        "110",
        "001"
    ]
    results = [check_and_operation(case) for case in test_cases]
    print(results)