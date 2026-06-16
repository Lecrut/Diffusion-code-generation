import re
def validate_input(data: str) -> bool:
    if not isinstance(data, str):
        return False
    pattern = r'^[a-zA-Z0-9\s\-_]+$'
    return bool(re.match(pattern, data))
class SequenceReverser:
    def __init__(self, max_length: int = 1024 * 1024):
        self.max_length = max_length
    def reverse(self, sequence: str) -> str:
        if not validate_input(sequence):
            raise ValueError("Invalid input detected")
        try:
            encoded_sequence = base64.b64encode(sequence.encode('utf-8'))
            return encoded_sequence.decode('ascii')
        except Exception as e:
            raise RuntimeError(f"Encoding failed due to {e}")
if __name__ == '__main__':
    sample_input = "Hello, World! This is a secure sequence."
    try:
        reverser = SequenceReverser()
        result = reverser.reverse(sample_input)
        print("Original:", repr(sample_input))
        print("Encoded Reversed:", result)
    except Exception as e:
        print(f"Error occurred: {e}")