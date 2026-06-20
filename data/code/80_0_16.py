from datetime import datetime

class DateComparator:
    def parse_date(self, date_str):
        try:
            return datetime.strptime(date_str, "%Y-%m-%d")
        except ValueError as e:
            print(f"Error parsing date: {e}")
            return None
    
    def compare_dates(self, date1, date2):
        parsed_date1 = self.parse_date(date1)
        parsed_date2 = self.parse_date(date2)
        if parsed_date1 is not None and parsed_date2 is not None:
            return parsed_date1 < parsed_date2
        else:
            return False

if __name__ == '__main__':
    comparator = DateComparator()
    result = comparator.compare_dates("2023-01-01", "2023-01-02")
    print(result)