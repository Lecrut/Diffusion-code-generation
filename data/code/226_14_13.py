from typing import TypeVar, Generic
T = TypeVar('T')

class Repeater(Generic[T]):

    def __init__(self, base: T):
        self.base = base

    def repeat(self, k: int) -> T:
        return self.base * k if isinstance(self.base, (str, bytes)) else [self.base] * k
if __name__ == '__main__':
    repeater_str = Repeater('X')
    print(repeater_str.repeat(5))
    repeater_list = Repeater([1, 2])
    print(repeater_list.repeat(3))