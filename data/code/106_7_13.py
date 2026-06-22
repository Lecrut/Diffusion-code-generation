from datetime import date

class DateCalculator:
    MIN_DAYS_IN_YEAR = 365
    MAX_DAYS_IN_YEAR = 366

    @staticmethod
    def _is_leap_year(year):
        return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

    @staticmethod
    def _days_in_year(year):
        return DateCalculator.MAX_DAYS_IN_YEAR if DateCalculator._is_leap_year(year) else DateCalculator.MIN_DAYS_IN_YEAR

    def calculate_full_years(self, start_date: date, end_date: date) -> int:
        if not isinstance(start_date, date) or not isinstance(end_date, date):
            raise ValueError("Inputs must be date objects")
        if start_date > end_date:
            raise ValueError("start_date must be before or equal to end_date")
        
        if start_date == end_date:
            return 0
        
        year_diff = end_date.year - start_date.year
        
        if year_diff == 0:
            return 0
        
        current_date = start_date
        full_years_count = 0
        
        while True:
            next_anniversary_year = current_date.year + 1
            try:
                next_anniversary = date(next_anniversary_year, current_date.month, current_date.day)
            except ValueError:
                next_anniversary = date(next_anniversary_year, 3, 1)
            
            if next_anniversary > end_date:
                break
            
            if next_anniversary <= end_date:
                full_years_count += 1
                current_date = next_anniversary
            else:
                break
        
        return full_years_count

if __name__ == '__main__':
    calculator = DateCalculator()
    start = date(1990, 5, 15)
    end = date(2023, 5, 14)
    result = calculator.calculate_full_years(start, end)
    print(result)