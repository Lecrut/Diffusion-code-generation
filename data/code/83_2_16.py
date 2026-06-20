import datetime

class DateComparator:
    def check_equality(self, date1, date2):
        if not isinstance(date1, datetime.date) or not isinstance(date2, datetime.date):
            raise ValueError("Both inputs must be instances of datetime.date")
        return date1 == date2

if __name__ == '__main__':
    comparator = DateComparator()
    result = comparator.check_equality(datetime.date(2023, 10, 5), datetime.date(2023, 10, 5))
    print(result)