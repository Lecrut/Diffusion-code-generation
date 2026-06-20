import datetime

class DateComparer:
    def __init__(self, date_str1, date_str2):
        try:
            self.date1 = datetime.datetime.strptime(date_str1, '%Y-%m-%d').date()
            self.date2 = datetime.datetime.strptime(date_str2, '%Y-%m-%d').date()
        except ValueError:
            raise ValueError("Invalid date format. Please use YYYY-MM-DD.")

    def are_dates_identical(self):
        return self.date1 == self.date2

if __name__ == '__main__':
    comparer1 = DateComparer("2023-10-26", "2023-10-26")
    print(f"Comparing dates: {comparer1.are_dates_identical()}")

    comparer2 = DateComparer("2023-10-26", "2023-10-27")
    print(f"Comparing dates: {comparer2.are_dates_identical()}")