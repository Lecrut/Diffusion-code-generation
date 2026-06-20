import datetime

class DateDifferenceCalculator:
    MIN_VALID_YEAR = 1
    MAX_VALID_YEAR = 9999
    
    @staticmethod
    def is_valid_date(year, month):
        try:
            datetime.date(year, month, 1)
            return True
        except ValueError:
            return False

    @classmethod
    def calculate_months_difference(cls, date1, date2):
        if not cls.is_valid_date(date1.year, date1.month) or not cls.is_valid_date(date2.year, date2.month):
            raise ValueError("Invalid date input")
        
        return abs((date2.year - date1.year) * 12 + (date2.month - date1.month))

if __name__ == '__main__':
    try:
        date1 = datetime.date(2022, 3, 15)
        date2 = datetime.date(2024, 10, 20)
        
        difference = DateDifferenceCalculator.calculate_months_difference(date1, date2)
        print(difference)
    except ValueError as e:
        print(e)