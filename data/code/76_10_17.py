from datetime import datetime

class DateCalculator:
    @staticmethod
    def validate_date(date_str):
        try:
            datetime.strptime(date_str, '%Y-%m-%d')
            return True
        except (TypeError, ValueError):
            return False

    @classmethod
    def get_difference(cls, date1_str, date2_str):
        if not cls.validate_date(date1_str) or not cls.validate_date(date2_str):
            raise ValueError("Invalid date format. Please use YYYY-MM-DD.")
        
        date1 = datetime.strptime(date1_str, '%Y-%m-%d')
        date2 = datetime.strptime(date2_str, '%Y-%m-%d')
        diff = abs(date1 - date2).days
        return diff

if __name__ == '__main__':
    calculator = DateCalculator()
    result1 = calculator.get_difference("2023-01-01", "2023-01-10")
    print(result1)
    
    try:
        result2 = calculator.get_difference("2024-12-31", "2024-01-01")
        print(result2)
    except ValueError as e:
        print(e)