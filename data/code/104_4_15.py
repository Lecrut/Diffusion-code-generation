class DateComparator:
    @staticmethod
    def are_same_date(date_tuple1, date_tuple2):
        return date_tuple1 == date_tuple2

if __name__ == '__main__':
    comparator = DateComparator()
    result = comparator.are_same_date((2023, 10, 25), (2023, 10, 25))
    print(result)