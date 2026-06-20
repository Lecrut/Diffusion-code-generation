from datetime import date

class DateComparator:
    def check_equality(self, date1, date2):
        if not isinstance(date1, date) or not isinstance(date2, date):
            raise ValueError("Both inputs must be of type 'date'")
        return date1 == date2

if __name__ == '__main__':
    comparator = DateComparator()
    result = comparator.check_equality(date(2023, 10, 5), date(2023, 10, 5))
    print(result)