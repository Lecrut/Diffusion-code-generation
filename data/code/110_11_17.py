from datetime import datetime

class DateSorter:
    def __init__(self, date_strings):
        self.date_strings = date_strings
        self.sorted_date_objects = None

    def sort_dates(self):
        self.sorted_date_objects = sorted([datetime.strptime(date_str, '%Y-%m-%d') for date_str in self.date_strings])

    def get_sorted_dates_as_strings(self):
        return [dt.strftime('%Y-%m-%d') for dt in self.sorted_date_objects] if self.sorted_date_objects else []

if __name__ == '__main__':
    sorter = DateSorter(["2023-10-26", "2023-10-25", "2023-10-27", "2023-10-24"])
    sorter.sort_dates()
    sorted_dates = sorter.get_sorted_dates_as_strings()
    print(sorted_dates)