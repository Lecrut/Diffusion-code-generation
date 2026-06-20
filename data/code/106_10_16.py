from datetime import datetime

class YearDifferenceCalculator:
    @staticmethod
    def calculate_year_difference(end_datetime: datetime, start_datetime: datetime) -> int:
        return abs((end_datetime.year - start_datetime.year))

if __name__ == '__main__':
    calc = YearDifferenceCalculator()
    end_date = datetime(2023, 12, 31)
    start_date = datetime(1990, 1, 1)
    difference = calc.calculate_year_difference(end_date, start_date)
    print(f"The difference between {end_date.year} and {start_date.year} is: {difference}")