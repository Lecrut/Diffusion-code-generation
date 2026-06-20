import datetime

class DateComparator:
    def __init__(self, date1: datetime.date, date2: datetime.date):
        self.date1 = date1
        self.date2 = date2

    def are_dates_identical(self) -> bool:
        return self.date1 == self.date2

if __name__ == '__main__':
    comparator_1 = DateComparator(datetime.date(2023, 10, 26), datetime.date(2023, 10, 26))
    comparator_2 = DateComparator(datetime.date(2023, 10, 26), datetime.date(2023, 10, 27))

    print(f"Are dates identical: {comparator_1.are_dates_identical()}")
    print(f"Are dates identical: {comparator_2.are_dates_identical()}")