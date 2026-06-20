class DateComparator:
    @staticmethod
    def check_equality(date1, date2):
        return date1 == date2

if __name__ == '__main__':
    from datetime import date
    date_a = date(2023, 10, 26)
    date_b = date(2023, 10, 26)
    result1 = DateComparator.check_equality(date_a, date_b)
    print(result1)