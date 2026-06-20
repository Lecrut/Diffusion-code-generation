import datetime

class DateComparator:
    @staticmethod
    def compare_dates(date1: datetime.date, date2: datetime.date) -> int:
        if date1 > date2:
            return 1
        elif date1 < date2:
            return -1
        else:
            return 0

if __name__ == '__main__':
    comparator = DateComparator()
    result = comparator.compare_dates(datetime.date(2023, 4, 1), datetime.date(2023, 3, 31))
    print(result)