from datetime import datetime

class DateDifferenceCalculator:
    @staticmethod
    def parse_date(date_str):
        return datetime.strptime(date_str, "%Y-%m-%d")

    @staticmethod
    def calculate_year_difference(date1, date2):
        date_obj1 = DateDifferenceCalculator.parse_date(date1)
        date_obj2 = DateDifferenceCalculator.parse_date(date2)
        year_diff = abs(date_obj1.year - date_obj2.year)
        return year_diff

if __name__ == '__main__':
    calculator = DateDifferenceCalculator()
    print(calculator.calculate_year_difference("2023-04-01", "1990-05-06"))
    print(calculator.calculate_year_difference("2000-01-01", "2024-12-31"))
    print(calculator.calculate_year_difference("1850-07-04", "1900-01-01"))