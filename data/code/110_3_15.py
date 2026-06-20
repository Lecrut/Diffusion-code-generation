from datetime import datetime

class DateSorter:
    def __init__(self, dates):
        self.dates = dates

    def sort_dates(self):
        return sorted(self.dates)

if __name__ == '__main__':
    sorter = DateSorter([
        datetime(2023, 1, 15),
        datetime(2022, 12, 31),
        datetime(2023, 5, 20),
        datetime(2021, 10, 10)
    ])
    sorted_dates = sorter.sort_dates()
    print(sorted_dates)