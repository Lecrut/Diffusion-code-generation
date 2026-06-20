from datetime import datetime

class DateComparator:
    DATE_FORMAT = '%Y-%m-%d'

    @staticmethod
    def compare_dates(date_str1, date_str2):
        try:
            date1 = datetime.strptime(date_str1, DateComparator.DATE_FORMAT)
            date2 = datetime.strptime(date_str2, DateComparator.DATE_FORMAT)
            return min(date1, date2)
        except ValueError:
            raise ValueError("Invalid date format provided. Dates must be in 'YYYY-MM-DD' format.")

if __name__ == '__main__':
    comparator = DateComparator()
    date_a = "2023-10-26"
    date_b = "2023-10-25"
    try:
        earlier_date = comparator.compare_dates(date_a, date_b)
        print(f"Comparing {date_a} and {date_b}: {earlier_date}")
    except ValueError as e:
        print(e)