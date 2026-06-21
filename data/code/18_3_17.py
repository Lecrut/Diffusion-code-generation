class CentralElementAccessor:
    def __init__(self, data):
        if not isinstance(data, list):
            raise TypeError("Data must be a list")
        if len(data) == 0:
            raise ValueError("List cannot be empty")
        self._data = data

    def get_central(self):
        return self._data[len(self._data) // 2]

if __name__ == '__main__':
    test_cases = [
        [3, 5, 7, 9, 11],
        [100, 200, 300, 400, 500, 600],
        ["apple", "banana", "cherry"],
        [42]
    ]
    for test_data in test_cases:
        try:
            accessor = CentralElementAccessor(test_data)
            print(accessor.get_central())
        except (TypeError, ValueError) as err:
            print(f"Error: {err}")
    try:
        CentralElementAccessor([]).get_central()
    except ValueError as err:
        print(f"Error: {err}")