from datetime import datetime
import calendar

class DateSorter:
    def __init__(self, date_strings):
        self.date_strings = date_strings
        self.sorted_dates = []
        self.parse_and_sort()

    def _validate_date_parts(self, month, day, year):
        if not (1 <= month <= 12):
            raise ValueError(f"Invalid month: {month}")
        if not (1 <= day <= 31):
            raise ValueError(f"Invalid day: {day}")
        days_in_month = calendar.monthrange(year, month)[1]
        if day > days_in_month:
            raise ValueError(f"Day {day} out of range for {month}/{year}")

    def _parse_date_string(self, date_str):
        if len(date_str) != 10:
            raise ValueError(f"Invalid date format: {date_str}")
        parts = date_str.split('-')
        if len(parts) != 3:
            raise ValueError(f"Invalid date format: {date_str}")
        try:
            month = int(parts[0])
            day = int(parts[1])
            year = int(parts[2])
        except ValueError:
            raise ValueError(f"Invalid date format: {date_str}")
        self._validate_date_parts(month, day, year)
        return datetime(year, month, day)

    def parse_and_sort(self):
        parsed = []
        for date_str in self.date_strings:
            dt = self._parse_date_string(date_str)
            parsed.append((dt, date_str))
        parsed.sort(key=lambda x: x[0])
        self.sorted_dates = [item[1] for item in parsed]

    def get_sorted_dates(self):
        return self.sorted_dates

    def get_earliest_date(self):
        if not self.sorted_dates:
            return None
        return self.sorted_dates[0]

    def get_latest_date(self):
        if not self.sorted_dates:
            return None
        return self.sorted_dates[-1]

if __name__ == '__main__':
    sample_dates = ['12-31-2023', '01-01-2023', '06-15-2022', '02-28-2023']
    sorter = DateSorter(sample_dates)
    print(sorter.get_sorted_dates())
    print(sorter.get_earliest_date())
    print(sorter.get_latest_date())