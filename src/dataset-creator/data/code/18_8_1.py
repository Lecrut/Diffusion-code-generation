import re
def validate_input(data: str) -> bool:
    if not isinstance(data, str):
        return False
    pattern = r'^[\w\s.,!?-]+$'
    return bool(re.match(pattern, data))
class SequenceReverser:
    def __init__(self, max_length: int = 10000):
        self.max_length = max_length
    def reverse(self, sequence: str) -> str:
        if not validate_input(sequence):
            raise ValueError("Invalid input detected")
        if len(sequence) > self.max_length:
            raise ValueError("Input exceeds maximum length limit")
        return ''.join(reversed(list(sequence)))
if __name__ == '__main__':
    sample_data = "Hello, World! This is a test sequence."
    reverser = SequenceReverser()
    try:
        result = reverser.reverse(sample_data)
        print(result)
    except ValueError as e:
        print(f"Error: {e}")