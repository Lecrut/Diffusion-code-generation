from typing import TypeVar, Sequence

T = TypeVar('T')

class LastItemAccessor:
    _NEGATIVE_ONE: int = -1

    @staticmethod
    def retrieve(container: Sequence[T]) -> T:
        return container[LastItemAccessor._NEGATIVE_ONE]

if __name__ == '__main__':
    data: list[int] = [1, 2, 3, 4, 5]
    output = LastItemAccessor.retrieve(data)
    print(output)