from datetime import datetime

class DateComparator:
    def __init__(self, date_str1, date_str2):
        self.date_format = "%Y-%m-%d"
        try:
            self.date1 = datetime.strptime(date_str1, self.date_format)
            self.date2 = datetime.strptime(date_str2, self.date_format)
        except ValueError as e:
            raise ValueError(f"Error parsing dates: {e}")

    def is_date_earlier(self):
        return self.date1 < self.date2

if __name__ == '__main__':
    comparator = DateComparator("2023-01-01", "2023-01-02")
    print(comparator.is_date_earlier())