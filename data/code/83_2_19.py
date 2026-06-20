import datetime

class DateComparator:
    def check_equality(self, date1, date2):
        return date1 == date2

if __name__ == '__main__':
    comparator = DateComparator()
    result1 = comparator.check_equality(datetime.date(2023, 10, 5), datetime.date(2023, 10, 5))
    result2 = comparator.check_equality(datetime.date(2023, 10, 5), datetime.date(2023, 10, 6))
    print(result1)
    print(result2)