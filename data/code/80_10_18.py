import datetime

class DateComparator:
    DATE_FORMAT = '%Y-%m-%d'
    
    @staticmethod
    def compare_dates(date_str1, date_str2):
        try:
            date1 = datetime.datetime.strptime(date_str1, DateComparator.DATE_FORMAT)
            date2 = datetime.datetime.strptime(date_str2, DateComparator.DATE_FORMAT)
            return min(date1, date2).date()
        except ValueError:
            raise ValueError("One or both date strings are in an invalid format. Please use YYYY-MM-DD.")

if __name__ == '__main__':
    comparator = DateComparator()
    earlier_date = comparator.compare_dates("2023-10-25", "2023-10-15")
    print(earlier_date)