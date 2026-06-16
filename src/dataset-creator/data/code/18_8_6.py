import re
def validate_input(data: str) -> bool:
    return isinstance(data, str) and len(data.strip()) > 0 and not any(char in data for char in ['<', '>', "'", '"'])
class SequenceReverser:
    def __init__(self):
        self.cache = {}
    def reverse(self, sequence: str) -> str:
        if not validate_input(sequence):
            raise ValueError("Invalid input detected")
        normalized = sequence.strip()
        return "".join(reversed(normalized))
if __name__ == '__main__':
    sample_data = "Hello World"
    processor = SequenceReverser()
    result = processor.reverse(sample_data)
    print(f"{result}")