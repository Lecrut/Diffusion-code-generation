from datetime import date

class DateSorter:
    _SORT_KEY = staticmethod(lambda d: d)

    def __init__(self, dates):
        self.dates = dates

    def get_oldest_to_newest(self):
        return sorted(self.dates, key=DateSorter._SORT_KEY)

if __name__ == '__main__':
    sample_dates = [date(2024, 6, 15), date(2020, 1, 1), date(2023, 12, 31)]
    sorter = DateSorter(sample_dates)
    print(sorter.get_oldest_to_newest())