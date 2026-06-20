class DateComparator:

    def check_equality(self, date1, date2):
        return date1 == date2
if __name__ == '__main__':
    comparator = DateComparator()
    print(comparator.check_equality(date(2023, 10, 5), date(2023, 10, 5)))
    print(comparator.check_equality(date(2023, 10, 5), date(2023, 10, 6)))