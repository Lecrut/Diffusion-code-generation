from typing import TypeVar, Generic, List

T = TypeVar('T')

class ListAccessor(Generic[T]):
    def get_head(self, sequence: List[T]) -> T:
        return sequence[0]

def retrieve_first_item(items: List[T]) -> T:
    accessor = ListAccessor[T]()
    return accessor.get_head(items)

if __name__ == '__main__':
    sample_values = [99, 101, 103]
    output = retrieve_first_item(sample_values)
    print(output)