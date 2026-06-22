from typing import Any

class SequenceRepeater:
    def __init__(self, base_sequence: str):
        self.base_sequence = base_sequence

    def repeat(self, k: int) -> str:
        if not isinstance(k, int) or k < 0:
            raise ValueError("k must be a non-negative integer")
        return self.base_sequence * k

if __name__ == '__main__':
    repeater = SequenceRepeater('X')
    result = repeater.repeat(5)
    print(result)