import datetime

class DateSorter:
    def __init__(self):
        self.formats = ['%m-%d-%Y']

    def parse_date(self, date_str):
        for fmt in self.formats:
            try:
                return datetime.datetime.strptime(date_str, fmt)
            except ValueError:
                continue
        raise ValueError("Date format not recognized")

    def sort_dates(self, date_strings):
        parsed_dates = [self.parse_date(date) for date in date_strings]
        sorted_dates = sorted(parsed_dates)
        return [date.strftime('%m-%d-%Y') for date in sorted_dates]

if __name__ == '__main__':
    sorter = DateSorter()
    dates = ['12-31-2020', '01-01-2021', '07-04-2020']
    sorted_dates = sorter.sort_dates(dates)
    print(sorted_dates)