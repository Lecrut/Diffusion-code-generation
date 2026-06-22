class ListAccessor:
    def __init__(self, data):
        self._data = data

    @staticmethod
    def _validate_length(data, minimum):
        if len(data) < minimum:
            raise ValueError(f"Collection length {len(data)} is less than required minimum {minimum}")

    def get_second_to_last(self):
        self._validate_length(self._data, 2)
        return self._data[-2]

if __name__ == '__main__':
    sample_numbers = [100, 200, 300, 400, 500]
    accessors = [
        ListAccessor(sample_numbers),
        ListAccessor(["x", "y", "z"]),
        ListAccessor([True, False, True, False])
    ]
    for accessor in accessors:
        print(accessor.get_second_to_last())
    try:
        ListAccessor([42]).get_second_to_last()
    except ValueError as e:
        print(e)
    try:
        ListAccessor([]).get_second_to_last()
    except ValueError as e:
        print(e)