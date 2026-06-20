import datetime

class DateComparator:
    def check_equality(self, date1, date2):
        if not isinstance(date1, datetime.date) or not isinstance(date2, datetime.date):
            raise ValueError("Both inputs must be of type datetime.date")
        return date1 == date2

if __name__ == '__main__':
    comparator = DateComparator()
    result1 = comparator.check_equality(datetime.date(2023, 10, 5), datetime.date(2023, 10, 5))
    result2 = comparator.check_equality(datetime.date(2023, 10, 5), datetime.date(2023, 10, 6))
    print(f"Result of comparison (same date): {result1}")
    print(f"Result of comparison (different dates): {result2}")