class DateSorter:
    def __init__(self, dates):
        self.dates = list(dates)

    def sort_chronologically(self):
        return sorted(self.dates)

    def get_first_date(self):
        return self.dates[0]

    def get_last_date(self):
        return self.dates[-1]

if __name__ == '__main__':
    sample_dates = [
        (2023, 10, 15),
        (2021, 5, 1),
        (2023, 1, 1),
        (2022, 12, 31),
        (2021, 5, 2)
    ]
    sorter = DateSorter(sample_dates)
    sorted_dates = sorter.sort_chronologically()
    print(sorted_dates)
    print(sorter.get_first_date())
    print(sorter.get_last_date())