class TimestampSorter:
    def __init__(self, timestamps):
        self.timestamps = list(timestamps)

    def sort(self):
        return sorted(self.timestamps)

if __name__ == '__main__':
    raw_data = [1625097600, 1577836800, 1609459200, 1546300800]
    sorter = TimestampSorter(raw_data)
    sorted_dates = sorter.sort()
    print(sorted_dates)