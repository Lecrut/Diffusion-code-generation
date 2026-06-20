import datetime

class DateComparator:
    DATE_FORMAT = "%Y-%m-%d"

    @staticmethod
    def parse_date(date_str):
        try:
            return datetime.datetime.strptime(date_str, DateComparator.DATE_FORMAT).date()
        except ValueError:
            raise ValueError("Invalid date format. Please use YYYY-MM-DD.")

    @staticmethod
    def compare_dates(date1, date2):
        if date1 < date2:
            return (date1, date2)
        elif date1 > date2:
            return (date2, date1)
        else:
            return (date1, date2)

if __name__ == '__main__':
    comparator = DateComparator()
    date_a = "2023-10-26"
    date_b = "2023-10-20"
    print(comparator.compare_dates(comparator.parse_date(date_a), comparator.parse_date(date_b)))