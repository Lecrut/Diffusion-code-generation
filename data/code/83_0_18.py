import datetime

class DateComparator:
    @staticmethod
    def are_dates_identical(date1: datetime.date, date2: datetime.date) -> bool:
        return date1 == date2

if __name__ == '__main__':
    date_a = datetime.date(2023, 10, 26)
    date_b = datetime.date(2023, 10, 26)
    date_c = datetime.date(2023, 10, 27)
    date_d = datetime.date(2023, 10, 26)
    
    comparator = DateComparator()
    
    print(f"Are {date_a} and {date_b} identical? {comparator.are_dates_identical(date_a, date_b)}")
    print(f"Are {date_a} and {date_c} identical? {comparator.are_dates_identical(date_a, date_c)}")
    print(f"Are {date_a} and {date_d} identical? {comparator.are_dates_identical(date_a, date_d)}")