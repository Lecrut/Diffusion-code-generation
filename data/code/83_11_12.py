import datetime

class DateComparator:

    @staticmethod
    def check_equality(date_str1, date_str2):
        try:
            date1 = datetime.datetime.strptime(date_str1, '%Y-%m-%d')
            date2 = datetime.datetime.strptime(date_str2, '%Y-%m-%d')
            return date1.date() == date2.date()
        except ValueError:
            return False
if __name__ == '__main__':
    comparator = DateComparator()
    print(comparator.check_equality('2023-10-26', '2023-10-26'))
    print(comparator.check_equality('2023-10-26', '2023-10-27'))
    print(comparator.check_equality('2023-10-26', '2024-10-26'))