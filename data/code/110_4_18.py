class DateSorter:
    def __init__(self, dates):
        if not isinstance(dates, (list, tuple)):
            raise ValueError("Input must be a list or tuple")
        self.dates = list(dates)

    def sort_chronologically(self):
        if not self.dates:
            return []
        return sorted(self.dates)

if __name__ == '__main__':
    raw_dates = [
        (1999, 12, 31),
        (2000, 1, 1),
        (2000, 1, 1),
        (1998, 2, 28),
        (2000, 12, 25)
    ]
    sorter = DateSorter(raw_dates)
    result = sorter.sort_chronologically()
    print(result)