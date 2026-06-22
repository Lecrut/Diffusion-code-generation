from datetime import date

class DateSorter:
    def __init__(self, dates):
        self.dates = dates

    def oldest_to_newest(self):
        return sorted([d for d in self.dates])

if __name__ == '__main__':
    sample_dates = [date(2022, 8, 10), date(2021, 3, 15), date(2023, 11, 20)]
    sorter = DateSorter(sample_dates)
    print(sorter.oldest_to_newest())
    print(len(sorter.dates))