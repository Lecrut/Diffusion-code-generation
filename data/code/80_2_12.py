import datetime

class DateComparator:
    DATE_FORMAT = "%Y-%m-%d"

    @staticmethod
    def parse_date(date_str):
        return datetime.datetime.strptime(date_str, DateComparator.DATE_FORMAT)

    def compare(self, date1_str, date2_str):
        date1 = self.parse_date(date1_str)
        date2 = self.parse_date(date2_str)
        if date1 < date2:
            return (date1_str, date2_str)
        else:
            return (date2_str, date1_str)

if __name__ == '__main__':
    comparator = DateComparator()
    date_a = "2023-01-15"
    date_b = "2023-01-01"
    result1 = comparator.compare(date_a, date_b)
    print(f"Comparing {date_a} and {date_b}: {result1}")