import datetime

class DateComparator:
    @staticmethod
    def check_equality(date_str1, date_str2):
        try:
            date1 = datetime.datetime.strptime(date_str1, '%Y-%m-%d')
            date2 = datetime.datetime.strptime(date_str2, '%Y-%m-%d')
            return date1.date() == date2.date()
        except ValueError as e:
            print(f"Invalid date format: {e}")
            return False

if __name__ == '__main__':
    comparator = DateComparator()
    result1 = comparator.check_equality("2023-10-26", "2023-10-26")
    result2 = comparator.check_equality("2023-10-27", "2023-10-26")
    result3 = comparator.check_equality("2024-10-26", "2023-10-26")
    print(f"Are '2023-10-26' and '2023-10-26' identical? {result1}")
    print(f"Are '2023-10-27' and '2023-10-26' identical? {result2}")
    print(f"Are '2024-10-26' and '2023-10-26' identical? {result3}")