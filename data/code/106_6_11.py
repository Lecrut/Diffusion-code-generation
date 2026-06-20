from datetime import datetime

class DateDifferenceCalculator:
    DATE_FORMAT = '%Y-%m-%d'

    @staticmethod
    def parse_date(date_str: str) -> datetime:
        try:
            return datetime.strptime(date_str, DateDifferenceCalculator.DATE_FORMAT)
        except ValueError as e:
            print(f'Error parsing date {date_str}: {e}')
            raise

    @staticmethod
    def calculate_years_difference(date1: datetime, date2: datetime) -> int:
        return abs((date2 - date1).days // 365)

if __name__ == '__main__':
    calculator = DateDifferenceCalculator()
    sample_date1 = '2000-01-01'
    sample_date2 = '2023-04-10'
    parsed_date1 = calculator.parse_date(sample_date1)
    parsed_date2 = calculator.parse_date(sample_date2)
    result = calculator.calculate_years_difference(parsed_date1, parsed_date2)
    print(result)