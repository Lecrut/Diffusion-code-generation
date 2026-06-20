class DateComparator:
    def check_equality(self, date1, date2):
        return date1 == date2

if __name__ == '__main__':
    comparator = DateComparator()
    date1 = '2023-10-05'
    date2 = '2023-10-05'
    print(comparator.check_equality(date1, date2))