import datetime

class DateComparator:
    def check_equality(self, date1_str, date2_str):
        date_format = "%Y-%m-%d"
        date1 = datetime.datetime.strptime(date1_str, date_format).date()
        date2 = datetime.datetime.strptime(date2_str, date_format).date()
        return date1 == date2

if __name__ == '__main__':
    comparator = DateComparator()
    print(comparator.check_equality("2023-10-26", "2023-10-26"))
    print(comparator.check_equality("2023-10-26", "2023-10-27"))
    print(comparator.check_equality("2024-01-01", "2023-10-26"))