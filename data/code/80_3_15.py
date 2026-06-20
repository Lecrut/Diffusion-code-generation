from datetime import datetime

class DateComparator:
    def __init__(self, date_str1, date_str2):
        self.date_str1 = date_str1
        self.date_str2 = date_str2
        self.date_format = "%Y-%m-%d"
        self.date1 = None
        self.date2 = None

    def parse_dates(self):
        try:
            self.date1 = datetime.strptime(self.date_str1, self.date_format)
            self.date2 = datetime.strptime(self.date_str2, self.date_format)
        except ValueError:
            raise ValueError("Error: Invalid date format provided.")

    def is_first_before_second(self):
        if not self.date1 or not self.date2:
            raise ValueError("Dates have not been parsed yet.")
        return self.date1 < self.date2

if __name__ == '__main__':
    comparator = DateComparator("2023-10-26", "2023-10-20")
    comparator.parse_dates()
    result = comparator.is_first_before_second()
    print(result)