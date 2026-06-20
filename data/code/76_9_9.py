import datetime

class DateCalculator:
    @staticmethod
    def parse_date(date_str: str) -> datetime.date:
        return datetime.datetime.strptime(date_str, "%Y-%m-%d").date()

    @staticmethod
    def calculate_difference(start_date_str: str, end_date_str: str) -> int:
        start_date = DateCalculator.parse_date(start_date_str)
        end_date = DateCalculator.parse_date(end_date_str)
        return abs((end_date - start_date).days)

if __name__ == '__main__':
    date_a = "2023-01-01"
    date_b = "2024-01-01"
    difference = DateCalculator.calculate_difference(date_a, date_b)
    print(difference)