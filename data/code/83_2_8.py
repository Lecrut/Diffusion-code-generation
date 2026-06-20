class DateComparator:
    def check_equality(self, date1, date2):
        return date1 == date2

if __name__ == '__main__':
    comparator = DateComparator()
    date1 = datetime.date(2023, 10, 5)
    date2 = datetime.date(2023, 10, 5)
    print(comparator.check_equality(date1, date2))