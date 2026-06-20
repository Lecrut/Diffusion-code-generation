class DateComparator:
    def check_equality(self, date1, date2):
        return date1 == date2

if __name__ == '__main__':
    comparator = DateComparator()
    result = comparator.check_equality(date(2023, 4, 1), date(2023, 4, 1))
    print(result)