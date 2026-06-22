from datetime import date
import calendar

class DateCalculator:
    MONTHS_IN_YEAR = 12

    @staticmethod
    def subtract_months(target_date, months_to_subtract):
        if not isinstance(target_date, date):
            raise ValueError("target_date must be a date object")
        if not isinstance(months_to_subtract, int):
            raise ValueError("months_to_subtract must be an integer")
        
        current_year = target_date.year
        current_month = target_date.month
        current_day = target_date.day
        
        total_months = current_year * DateCalculator.MONTHS_IN_YEAR + current_month
        new_total_months = total_months - months_to_subtract
        
        if new_total_months <= 0:
            raise ValueError("Resulting date would be before year 1")
            
        new_year = (new_total_months - 1) // DateCalculator.MONTHS_IN_YEAR + 1
        new_month = (new_total_months - 1) % DateCalculator.MONTHS_IN_YEAR + 1
        
        max_day_in_new_month = calendar.monthrange(new_year, new_month)[1]
        adjusted_day = min(current_day, max_day_in_new_month)
        
        return date(new_year, new_month, adjusted_day)

if __name__ == '__main__':
    original_date = date(2023, 10, 15)
    result = DateCalculator.subtract_months(original_date, 3)
    print(result)