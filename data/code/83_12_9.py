from datetime import datetime

class DateComparison:
    DATE_FORMAT = "%Y-%m-%d"

    @staticmethod
    def are_dates_equal(date_str1, date_str2):
        try:
            return datetime.strptime(date_str1, DateComparison.DATE_FORMAT) == datetime.strptime(date_str2, DateComparison.DATE_FORMAT)
        except ValueError:
            return False

if __name__ == '__main__':
    comparison = DateComparison()
    date_a = "2023-10-27"
    date_b = "2023-10-28"
    print(f"Comparing {date_a} and {date_b}: {comparison.are_dates_equal(date_a, date_b)}")