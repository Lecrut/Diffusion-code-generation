import datetime

class DateComparator:
    @staticmethod
    def difference_in_days(date1, date2):
        if not isinstance(date1, datetime.datetime) or not isinstance(date2, datetime.datetime):
            raise ValueError("Both inputs must be instances of datetime.datetime")
        
        delta = abs(date1 - date2)
        return delta.days

if __name__ == '__main__':
    d1 = datetime.datetime(2023, 10, 26, 10, 30, 0)
    d2 = datetime.datetime(2023, 10, 25, 15, 45, 0)
    d3 = datetime.datetime(2024, 1, 1, 0, 0, 0)
    d4 = datetime.datetime(2024, 1, 1, 0, 0, 0)

    print(DateComparator.difference_in_days(d1, d2))
    print(DateComparator.difference_in_days(d3, d4))
    print(DateComparator.difference_in_days(d2, d1))
    print(DateComparator.difference_in_days(d4, d3))
    print(DateComparator.difference_in_days(d1, d1))