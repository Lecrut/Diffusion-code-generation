import datetime

class DateComparator:
    DATE_FORMAT = '%Y-%m-%d'

    @staticmethod
    def are_dates_identical(date1, date2):
        try:
            return date1.date() == date2.date()
        except AttributeError:
            return False

if __name__ == '__main__':
    date_a = datetime.datetime(2023, 10, 26)
    date_b = datetime.datetime(2023, 10, 26)
    date_c = datetime.datetime(2023, 10, 27)
    
    print(f"Comparing {date_a} and {date_b}: {DateComparator.are_dates_identical(date_a, date_b)}")
    print(f"Comparing {date_a} and {date_c}: {DateComparator.are_dates_identical(date_a, date_c)}")