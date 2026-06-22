class DateSorter:
    def __init__(self, dates):
        self.dates = list(dates)
        self._sorted_dates = None

    def sort_chronologically(self):
        if self._sorted_dates is not None:
            return self._sorted_dates
        n = len(self.dates)
        if n == 0:
            self._sorted_dates = []
            return self._sorted_dates
        indices = list(range(n))
        for i in range(n):
            for j in range(i + 1, n):
                if self._compare(indices[i], indices[j]) > 0:
                    indices[i], indices[j] = indices[j], indices[i]
        self._sorted_dates = [self.dates[idx] for idx in indices]
        return self._sorted_dates

    def get_sorted_dates(self):
        return self.sort_chronologically()

    def get_unsorted_dates(self):
        return list(self.dates)

    def _compare(self, i, j):
        y1, m1, d1 = self.dates[i]
        y2, m2, d2 = self.dates[j]
        if y1 != y2:
            return y1 - y2
        if m1 != m2:
            return m1 - m2
        return d1 - d2

if __name__ == '__main__':
    raw_dates = [
        (2023, 10, 15),
        (1999, 1, 1),
        (2023, 1, 1),
        (2023, 10, 1),
        (1999, 12, 31)
    ]
    sorter = DateSorter(raw_dates)
    print(sorter.get_unsorted_dates())
    print(sorter.get_sorted_dates())
    print(sorter.get_sorted_dates())