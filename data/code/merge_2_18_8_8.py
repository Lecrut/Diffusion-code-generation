import re
def validate_input(data: str) -> bool:
    if not isinstance(data, str):
        return False
    pattern = r'^[a-zA-Z0-9\s\-_]+$'
    try:
        is_valid = bool(re.match(pattern, data))
        if not is_valid or len(data.strip()) == 0:
            raise ValueError("Invalid input format")
        return True
    except Exception as e:
        print(f"Validation error: {e}")
        return False
def reverse_sequence(sequence: str) -> str:
    reversed_seq = sequence[::-1]
    if len(reversed_seq.strip()) == 0:
        raise ValueError("Empty input")
    return reversed_seq
if __name__ == '__main__':
    sample_inputs = ["Hello World!", "Python3.9", "", "<script>alert('xss')</script>", "!@#$%^&*()"]
    for test_data in sample_inputs:
        if validate_input(test_data):
            try:
                result = reverse_sequence(test_data)
                print(f"Input: '{test_data}' -> Output: '{result}'")
            except ValueError as ve:
                print(f"Processing error for input '{test_data}': {ve}")
        else:
            print(f"Ignoring invalid input: '{test_data}'")