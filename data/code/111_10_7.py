from datetime import datetime

class DateDifferenceCalculator:
    DATE_FORMAT = '%Y-%m-%d'

    @staticmethod
    def parse_date(date_str):
        return datetime.strptime(date_str, DateDifferenceCalculator.DATE_FORMAT)

    @staticmethod
    def calculate_difference(date1, date2):
        return abs((date2 - date1).days)

if __name__ == '__main__':
    date1 = "2023-10-01"
    date2 = "2023-10-15"
    print(f"Date 1: {date1}")
    print(f"Date 2: {date2}")
    parsed_date1 = DateDifferenceCalculator.parse_date(date1)
    parsed_date2 = DateDifferenceCalculator.parse_date(date2)
    difference = DateDifferenceCalculator.calculate_difference(parsed_date1, parsed_date2)
    print(f"Days between {date1} and {date2}: {difference}")