from datetime import datetime

class DateDifferenceCalculator:
    DATE_FORMAT = "%m/%d/%Y"

    @staticmethod
    def parse_date(date_str):
        try:
            return datetime.strptime(date_str, DateDifferenceCalculator.DATE_FORMAT)
        except ValueError:
            raise ValueError(f"Invalid date format: {date_str}. Please use MM/DD/YYYY.")

    @classmethod
    def calculate_difference(cls, date1_str, date2_str):
        date1 = cls.parse_date(date1_str)
        date2 = cls.parse_date(date2_str)
        return abs((date2 - date1).days)

if __name__ == '__main__':
    calculator = DateDifferenceCalculator()
    result = calculator.calculate_difference('01/01/2023', '01/10/2023')
    print(result)