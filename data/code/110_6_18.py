class ChronologicalSorter:
    def __init__(self, timestamps):
        if not isinstance(timestamps, (list, tuple)):
            raise ValueError("Input must be a sequence")
        self.timestamps = list(timestamps)

    def sort(self):
        if not self.timestamps:
            return []
        return sorted(self.timestamps)

if __name__ == '__main__':
    data = [1609459200, 1577836800, 1625097600, 1546300800]
    sorter = ChronologicalSorter(data)
    print(sorter.sort())