class UnixTimestampSorter:
    def __init__(self, timestamps):
        self._validate_input(timestamps)
        self.timestamps = list(timestamps)

    def _validate_input(self, data):
        if not isinstance(data, (list, tuple)):
            raise ValueError("Input must be a list or tuple")
        for idx, val in enumerate(data):
            if not isinstance(val, int):
                raise ValueError(f"Element at index {idx} is not an integer")
            if val < 0:
                raise ValueError(f"Timestamp at index {idx} cannot be negative")

    def get_sorted(self):
        return sorted(self.timestamps)

    def get_oldest(self):
        if not self.timestamps:
            return None
        return min(self.timestamps)

    def get_newest(self):
        if not self.timestamps:
            return None
        return max(self.timestamps)

if __name__ == '__main__':
    raw_data = [1640995200, 1577836800, 1704067200, 1609459200]
    sorter = UnixTimestampSorter(raw_data)
    print(sorter.get_sorted())
    print(sorter.get_oldest())
    print(sorter.get_newest())