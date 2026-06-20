class DateSorter:
    def __init__(self):
        self.sample_dates = [(2023, 1, 15), (2022, 12, 25), (2024, 1, 1)]

    def sort_dates(self):
        return sorted(self.sample_dates)

if __name__ == '__main__':
    sorter = DateSorter()
    sorted_dates = sorter.sort_dates()
    print("Sorted Dates:")
    for date in sorted_dates:
        print(date)