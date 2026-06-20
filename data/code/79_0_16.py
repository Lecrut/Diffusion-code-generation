import datetime

class DateCalculator:
    MONTHS_IN_YEAR = 12
    
    @staticmethod
    def calculate_next_month(start_date):
        year = start_date.year
        month = start_date.month
        day = start_date.day
        
        if month == DateCalculator.MONTHS_IN_YEAR:
            next_month = 1
            next_year = year + 1
        else:
            next_month = month + 1
            next_year = year
        
        try:
            return datetime.date(next_year, next_month, day)
        except ValueError:
            if month == 2 and day > 28:
                return datetime.date(next_year, next_month, 28)

if __name__ == '__main__':
    start_date_str = "2023-12-31"
    start_date = datetime.datetime.strptime(start_date_str, "%Y-%m-%d").date()
    calculator = DateCalculator()
    next_date = calculator.calculate_next_month(start_date)
    print(next_date.strftime("%Y-%m-%d"))