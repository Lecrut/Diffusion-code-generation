from typing import TypeVar
T = TypeVar('T')

class SequenceRepeater:

    def __init__(self, base_sequence: T):
        if not isinstance(base_sequence, (list, str)):
            raise ValueError('Base sequence must be a list or string')
        self.base_sequence = base_sequence

    def repeat(self, k: int) -> T:
        if not isinstance(k, int) or k < 0:
            raise ValueError('Repeat count must be a non-negative integer')
        return self.base_sequence * k
if __name__ == '__main__':
    repeater = SequenceRepeater('X')
    result = repeater.repeat(5)
    print(result)