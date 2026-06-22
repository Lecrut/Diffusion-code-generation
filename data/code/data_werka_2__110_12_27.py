class DateSorter:
    def __init__(self, dates):
        self.dates = list(dates)
        self.sorted_dates = []
        self._sort()

    def _sort(self):
        n = len(self.dates)
        for i in range(n):
            min_idx = i
            for j in range(i + 1, n):
                current = self.dates[j]
                candidate = self.dates[min_idx]
                if current < candidate:
                    min_idx = j
            self.dates[i], self.dates[min_idx] = self.dates[min_idx], self.dates[i]
        self.sorted_dates = self.dates

    def get_sorted(self):
        return self.sorted_dates

    def get_unsorted(self):
        return self.dates

    def count(self):
        return len(self.sorted_dates)

if __name__ == '__main__':
    raw_dates = [
        (2024, 5, 12),
        (1980, 12, 25),
        (2024, 5, 12),
        (2000, 2, 29),
        (1999, 1, 1)
    ]
    sorter = DateSorter(raw_dates)
    print(sorter.get_sorted())
    print(sorter.count())
    print(sorter.get_unsorted())