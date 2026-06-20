from datetime import datetime

class DateComparator:
    DATE_FORMAT = "%Y-%m-%d"
    
    @staticmethod
    def parse_date(date_str):
        try:
            return datetime.strptime(date_str, DateComparator.DATE_FORMAT)
        except ValueError:
            raise ValueError(f"Invalid date format: {date_str}")
    
    def compare_dates(self, date_str1, date_str2):
        return self.parse_date(date_str1) == self.parse_date(date_str2)

if __name__ == '__main__':
    comparator = DateComparator()
    date_a = "2023-10-27"
    date_b = "2023-10-28"
    print(f"Comparing {date_a} and {date_b}: {comparator.compare_dates(date_a, date_b)}")