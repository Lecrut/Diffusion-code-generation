from datetime import date

class WeekDifferenceCalculator:
    WEEK_DAYS = 7
    
    @staticmethod
    def validate_date(date_obj):
        if not isinstance(date_obj, date):
            raise ValueError("Input must be an instance of date.")
    
    @classmethod
    def order_dates(cls, date1, date2):
        if date1 > date2:
            return date2, date1
        return date1, date2
    
    @staticmethod
    def calculate_weeks(date1, date2):
        return (date2 - date1).days // 7
    
    def __init__(self, start_date: date, end_date: date):
        self.validate_date(start_date)
        self.validate_date(end_date)
        self.start_date, self.end_date = self.order_dates(start_date, end_date)
    
    def get_week_difference(self) -> int:
        return self.calculate_weeks(self.start_date, self.end_date)

if __name__ == '__main__':
    calculator1 = WeekDifferenceCalculator(date(2023, 1, 1), date(2023, 1, 8))
    print(calculator1.get_week_difference())
    
    calculator2 = WeekDifferenceCalculator(date(2023, 1, 8), date(2023, 1, 1))
    print(calculator2.get_week_difference())
    
    calculator3 = WeekDifferenceCalculator(date(2023, 1, 1), date(2023, 2, 1))
    print(calculator3.get_week_difference())
    
    calculator4 = WeekDifferenceCalculator(date(2023, 12, 25), date(2024, 1, 1))
    print(calculator4.get_week_difference())