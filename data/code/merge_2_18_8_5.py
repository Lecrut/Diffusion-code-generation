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
            return f"Reversed Sequence (Base64 Encoded): {decoded_reversed}"
        except Exception as e:
            raise RuntimeError(f"Processing error occurred: {str(e)}")
if __name__ == '__main__':
    sample_data = "Hello, World! This is a test string."
    try:
        reverser = SequenceReverser()
        result = reverser.reverse(sample_data)
        print(result)
    except ValueError as ve:
        print(f"Validation Error: {ve}")
    except RuntimeError as re:
        print(f"Runtime Error: {re}")