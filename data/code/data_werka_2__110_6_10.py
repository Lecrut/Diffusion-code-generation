class TimestampSorter:
    def __init__(self, timestamps):
        self.timestamps = list(timestamps)
        self.is_sorted = False

    def sort_ascending(self):
        if not self.is_sorted:
            self.timestamps.sort()
            self.is_sorted = True
        return self.timestamps

    def get_middle_element(self):
        if not self.timestamps:
            return None
        n = len(self.timestamps)
        return self.timestamps[n // 2]

    def get_min_max(self):
        if not self.timestamps:
            return (None, None)
        return (self.timestamps[0], self.timestamps[-1])

if __name__ == '__main__':
    raw_timestamps = [1700000000, 1600000000, 1800000000, 1500000000, 1650000000]
    sorter = TimestampSorter(raw_timestamps)
    sorted_list = sorter.sort_ascending()
    print(sorted_list)
    print(sorter.get_middle_element())
    print(sorter.get_min_max())