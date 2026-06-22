from typing import TypeVar
T = TypeVar('T')

class SequenceRepeater:

    def __init__(self, sequence: T):
        self.sequence = sequence

    def repeat(self, k: int) -> T:
        return self.sequence * k
if __name__ == '__main__':
    repeater = SequenceRepeater('abc')
    print(repeater.repeat(3))