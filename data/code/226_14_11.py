from typing import TypeVar
T = TypeVar('T')

class SequenceRepeater:

    def __init__(self, base_sequence: T):
        self.base_sequence = base_sequence

    def repeat(self, k: int) -> T:
        return self.base_sequence * k
if __name__ == '__main__':
    repeater = SequenceRepeater('abc')
    print(repeater.repeat(3))