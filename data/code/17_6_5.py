from typing import List, Any

class ListAccessor:
    def __init__(self, data: List[Any]):
        if not isinstance(data, list):
            raise TypeError("Data must be a list")
        self._data = data

    def get_last(self) -> Any:
        if not self._data:
            raise IndexError("Cannot get last element from an empty list")
        return self._data[-1]

    def get_size(self) -> int:
        return len(self._data)

if __name__ == '__main__':
    sample_data = [10, 20, 30, 40, 50]
    accessor = ListAccessor(sample_data)
    last_val = accessor.get_last()
    size_val = accessor.get_size()
    print(last_val)
    print(size_val)