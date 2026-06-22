class TimestampSorter:
    MIN_TIMESTAMP = 0
    DEFAULT_SAMPLE = [1609459200, 1577836800, 1625097600, 1546300800]

    def sort(self, timestamps):
        if not isinstance(timestamps, list):
            raise ValueError("Input must be a list")
        if not all(isinstance(ts, int) for ts in timestamps):
            raise ValueError("All elements must be integers")
        return sorted(timestamps)

if __name__ == '__main__':
    sorter = TimestampSorter()
    sample_data = [1700000000, 1600000000, 1800000000, 1500000000, 1650000000]
    result = sorter.sort(sample_data)
    print(result)