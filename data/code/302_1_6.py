class MonthDaysCalculator:
    def __init__(self):
        self.month_days = {
            1: 31, 2: 28, 3: 31, 4: 30, 
            5: 31, 6: 30, 7: 31, 8: 31, 
            9: 30, 10: 31, 11: 30, 12: 31
        }

    def is_leap_year(self, year):
        return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

    def get_days_in_month(self, year, month):
        if not 1 <= month <= 12:
            raise ValueError("Invalid month")
        
        days = self.month_days[month]
        if month == 2 and self.is_leap_year(year):
            days += 1
        return days

if __name__ == '__main__':
    calculator = MonthDaysCalculator()
    
    result1 = calculator.get_days_in_month(2020, 2)
    print(f"Days in February 2020: {result1}")
    
    result2 = calculator.get_days_in_month(2019, 2)
    print(f"Days in February 2019: {result2}")
    
    result3 = calculator.get_days_in_month(2021, 4)
    print(f"Days in April 2021: {result3}")