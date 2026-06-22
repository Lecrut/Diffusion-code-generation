from typing import List

class SequenceRepeater:
    def __init__(self, base_sequence: str):
        self.base_sequence = base_sequence

    def repeat(self, k: int) -> str:
        return self.base_sequence * k

if __name__ == '__main__':
    repeater = SequenceRepeater('X')
    result = repeater.repeat(5)
    print(result)