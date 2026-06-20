import datetime

class DateSorter:
    def __init__(self):
        self.dates = []

    def add_date(self, date_str):
        try:
            date_obj = datetime.datetime.strptime(date_str, '%Y-%m-%d')
            self.dates.append(date_obj)
        except ValueError:
            print(f"Skipping invalid date format: {date_str}")

    def sort_dates(self):
        return sorted(self.dates)

if __name__ == '__main__':
    sorter = DateSorter()
    sample_dates = ['2023-01-01', '2022-12-31', '2023-04-01']
    for date in sample_dates:
        sorter.add_date(date)
    sorted_dates = sorter.sort_dates()
    print(sorted_dates)