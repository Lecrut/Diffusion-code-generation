from datetime import date
class DateSorter:
    def __init__(self, dates):
        self.dates = dates
    def oldest_first(self):
        return sorted(self.dates)
    def newest_first(self):
        return sorted(self.dates, reverse=True)
if __name__ == '__main__':
    samples = [date(2024, 6, 1), date(2020, 1, 1), date(2022, 8, 15)]
    sorter = DateSorter(samples)
    print(sorter.oldest_first())
    print(sorter.newest_first())