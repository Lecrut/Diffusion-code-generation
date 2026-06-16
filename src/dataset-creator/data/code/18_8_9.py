import re
def validate_input(data: str) -> bool:
    if not isinstance(data, str):
        return False
    pattern = r'^[\w\s.,!?-]+$'
    return bool(re.match(pattern, data))
class SequenceReverser:
    def __init__(self):
        self.max_length = 1024
    def reverse(self, sequence: str) -> str:
        if not validate_input(sequence):
            raise ValueError("Invalid input detected")
        try:
            encoded_sequence = base64.b64encode(sequence.encode('utf-8')).decode('ascii')
            decoded_reversed = base64.b64decode(encoded_sequence).decode('utf-8')[::-1]
            return f"Reversed Sequence (Base64 Encoded): {encoded_sequence}"
        except Exception:
            raise ValueError("Malformed input or encoding error")
if __name__ == '__main__':
    sample_input = "Hello, World! This is a test."
    try:
        reverser = SequenceReverser()
        result = reverser.reverse(sample_input)
        print(result)
    except ValueError as e:
        print(f"Error: {e}")