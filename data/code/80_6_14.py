from datetime import date

class DateComparator:
    def __init__(self, date_str1, date_obj2):
        self.date_str1 = date_str1
        self.date_obj2 = date_obj2

    @staticmethod
    def parse_date_string(date_str):
        parts = date_str.split('-')
        if len(parts) != 3:
            raise ValueError("Date string must be in 'YYYY-MM-DD' format.")
        return date(int(parts[0]), int(parts[1]), int(parts[2]))

    def compare_dates(self):
        parsed_date_str1 = self.parse_date_string(self.date_str1)
        if parsed_date_str1 < self.date_obj2:
            return parsed_date_str1
        else:
            return self.date_obj2

if __name__ == '__main__':
    comparator = DateComparator('2023-04-01', date(2023, 5, 1))
    earlier_date = comparator.compare_dates()
    print(earlier_date)