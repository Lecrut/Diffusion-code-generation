from typing import TypeVar, Generic

T = TypeVar('T')

class Repeater(Generic[T]):
    def __init__(self, sequence: T):
        self.sequence = sequence
    
    def repeat(self, k: int) -> T:
        return self.sequence * k

if __name__ == '__main__':
    sample_sequence = 'X'
    repeater = Repeater(sample_sequence)
    result = repeater.repeat(5)
    print(result)