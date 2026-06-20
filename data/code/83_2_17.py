from datetime import date

class DateComparator:
    def check_equality(self, date1: date, date2: date) -> bool:
        return date1 == date2

if __name__ == '__main__':
    comparator = DateComparator()
    result = comparator.check_equality(date(2023, 10, 5), date(2023, 10, 5))
    print(result)