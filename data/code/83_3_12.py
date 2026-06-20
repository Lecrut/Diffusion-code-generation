class DateComparator:
    def check_equality(self, date1, date2):
        return date1 == date2

if __name__ == '__main__':
    comparator = DateComparator()
    result1 = comparator.check_equality(date(2023, 10, 26), date(2023, 10, 26))
    print(result1)
    result2 = comparator.check_equality(date(2023, 10, 26), date(2023, 10, 27))
    print(result2)