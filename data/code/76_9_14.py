import datetime

class DateCalculator:
    @staticmethod
    def parse_date(date_str: str) -> datetime.date:
        return datetime.datetime.strptime(date_str, '%Y-%m-%d').date()

    @staticmethod
    def calculate_difference(start_date: str, end_date: str) -> int:
        start = DateCalculator.parse_date(start_date)
        end = DateCalculator.parse_date(end_date)
        return abs((end - start).days)

if __name__ == '__main__':
    date_a = '2023-01-01'
    date_b = '2024-01-01'
    difference = DateCalculator.calculate_difference(date_a, date_b)
    print(difference)