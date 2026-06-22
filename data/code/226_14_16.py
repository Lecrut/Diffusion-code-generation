from typing import TypeVar, Generic
T = TypeVar('T')

class SequenceRepeater(Generic[T]):

    def __init__(self, base: T):
        self.base = base

    def repeat(self, k: int) -> T:
        return self.base * k
if __name__ == '__main__':
    repeater = SequenceRepeater('abc')
    print(repeater.repeat(3))