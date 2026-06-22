class MonthDaysCalculator:
    _days_per_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    @staticmethod
    def is_leap_year(year):
        return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
    
    def days_in_month(self, year, month):
        if not (1 <= year <= 9999) or not (1 <= month <= 12):
            raise ValueError('Year must be between 1 and 9999, and month must be between 1 and 12')
        
        days = self._days_per_month[month - 1]
        if month == 2 and self.is_leap_year(year):
            days += 1
        
        return days

if __name__ == '__main__':
    calculator = MonthDaysCalculator()
    print(calculator.days_in_month(2023, 2))
    print(calculator.days_in_month(2024, 2))
    print(calculator.days_in_month(2023, 4))