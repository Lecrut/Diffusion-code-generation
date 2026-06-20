import datetime

class DateComparator:
    def check_equality(self, date1, date2):
        return date1.date() == date2.date()

if __name__ == '__main__':
    comparator = DateComparator()
    result = comparator.check_equality(datetime.datetime(2023, 10, 5), datetime.datetime(2023, 10, 5))
    print(result)