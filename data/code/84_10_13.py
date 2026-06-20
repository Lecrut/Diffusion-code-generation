class DateCalculator:
    def __init__(self):
        self.month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    def is_leap_year(self, year):
        return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
    
    def get_day_of_year(self, year, month, day):
        if month < 1 or month > 12:
            raise ValueError("Month must be between 1 and 12.")
        if day < 1 or day > self.month_days[month - 1] + (self.is_leap_year(year) and month == 2):
            raise ValueError(f"Day is out of range for the specified month and year.")
        
        total_days = sum(self.month_days[:month - 1])
        if self.is_leap_year(year) and month > 2:
            total_days += 1
        total_days += day
        
        return total_days

if __name__ == '__main__':
    calculator = DateCalculator()
    year = 2023
    month = 10
    day = 27
    print(calculator.get_day_of_year(year, month, day))