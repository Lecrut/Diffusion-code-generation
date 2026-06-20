import datetime

class DateComparator:
    def check_equality(self, date1: datetime.date, date2: datetime.date) -> bool:
        return date1 == date2

if __name__ == '__main__':
    comparator = DateComparator()
    date1 = datetime.date(2023, 10, 5)
    date2 = datetime.date(2023, 10, 5)
    date3 = datetime.date(2023, 10, 6)

    print(f"Comparing {date1} and {date2}: {comparator.check_equality(date1, date2)}")
    print(f"Comparing {date1} and {date3}: {comparator.check_equality(date1, date3)}")
    print(f"Comparing {date2} and {date3}: {comparator.check_equality(date2, date3)}")