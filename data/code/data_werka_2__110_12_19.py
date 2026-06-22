class DateSorter:
    def __init__(self, dates):
        self.dates = list(dates)

    def sort_chronologically(self):
        n = len(self.dates)
        if n <= 1:
            return self.dates
        
        for i in range(1, n):
            key = self.dates[i]
            j = i - 1
            while j >= 0:
                prev = self.dates[j]
                if prev[0] > key[0] or \
                   (prev[0] == key[0] and prev[1] > key[1]) or \
                   (prev[0] == key[0] and prev[1] == key[1] and prev[2] > key[2]):
                    self.dates[j + 1] = self.dates[j]
                    j -= 1
                else:
                    break
            self.dates[j + 1] = key
        return self.dates

    def get_first_date(self):
        if not self.dates:
            return None
        return self.dates[0]

    def get_last_date(self):
        if not self.dates:
            return None
        return self.dates[-1]

if __name__ == '__main__':
    sample_dates = [
        (2023, 10, 15),
        (1999, 1, 1),
        (2023, 1, 1),
        (2023, 10, 1),
        (1999, 12, 31),
        (2000, 2, 29)
    ]
    sorter = DateSorter(sample_dates)
    sorted_result = sorter.sort_chronologically()
    print(sorted_result)
    print(sorter.get_first_date())
    print(sorter.get_last_date())