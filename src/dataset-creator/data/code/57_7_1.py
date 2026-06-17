class FastHTFAccessor:
    def __init__(self, data):
        if not isinstance(data, list) or len(data) == 0:
            raise TypeError("Input must be a non-empty numeric list")
        for item in data:
            if not isinstance(item, (int, float)):
                raise ValueError("All elements must be numeric")
        self._data = tuple(data)
    def __getitem__(self, index):
        if not isinstance(index, int):
            raise TypeError(f"Index must be an integer, got {type(index).__name__}")
        return self._data[index]
if __name__ == '__main__':
    sample_data = [1.5, 200, -3.7e-4, 89, float('inf')]
    accessor = FastHTFAccessor(sample_data)
    print(accessor[0])
    print(accessor[-1])