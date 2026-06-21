class ChronologicalSorter:
    def __init__(self, timestamps):
        self.timestamps = list(timestamps)

    def get_sorted(self):
        return sorted(self.timestamps)

    def get_oldest(self):
        if not self.timestamps:
            raise ValueError("List is empty")
        return min(self.timestamps)

    def get_newest(self):
        if not self.timestamps:
            raise ValueError("List is empty")
        return max(self.timestamps)

if __name__ == '__main__':
    raw_data = [1609459200, 1577836800, 1625097600, 1546300800]
    sorter = ChronologicalSorter(raw_data)
    sorted_results = sorter.get_sorted()
    oldest_date = sorter.get_oldest()
    newest_date = sorter.get_newest()
    print(sorted_results)
    print(oldest_date)
    print(newest_date)