class DateComparator:
    def check_equality(self, date1, date2):
        return date1 == date2
if __name__ == '__main__':
    class Date:
        def __init__(self, year, month, day):
            self.year = year
            self.month = month
            self.day = day
        def __eq__(self, other):
            if isinstance(other, Date):
                return self.year == other.year and self.month == other.month and self.day == other.day
            return False
        def __repr__(self):
            return f"Date({self.year}, {self.month}, {self.day})"
    date_a = Date(2023, 10, 26)
    date_b = Date(2023, 10, 26)
    date_c = Date(2023, 10, 27)
    comparator = DateComparator()
    result1 = comparator.check_equality(date_a, date_b)
    result2 = comparator.check_equality(date_a, date_c)
    print(f"date_a: {date_a}")
    print(f"date_b: {date_b}")
    print(f"date_c: {date_c}")
    print(f"Equality of date_a and date_b: {result1}")
    print(f"Equality of date_a and date_c: {result2}")