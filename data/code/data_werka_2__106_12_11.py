from datetime import date
import calendar

class DateCalculator:
    DAYS_IN_COMMON_YEAR = 365
    DAYS_IN_LEAP_YEAR = 366

    @staticmethod
    def _is_leap_year(year: int) -> bool:
        return calendar.isleap(year)

    @staticmethod
    def days_in_year(year: int) -> int:
        return DateCalculator.DAYS_IN_LEAP_YEAR if DateCalculator._is_leap_year(year) else DateCalculator.DAYS_IN_COMMON_YEAR

    @classmethod
    def calculate_years_between(cls, start_date: date, end_date: date) -> float:
        if start_date > end_date:
            raise ValueError("start_date must be before or equal to end_date")
        
        delta_days = (end_date - start_date).days
        total_years = 0.0
        
        current_year = start_date.year
        
        while current_year < end_date.year:
            days_in_current_year = cls.days_in_year(current_year)
            remaining_days_in_year = days_in_current_year - start_date.timetuple().tm_yday
            
            if delta_days >= remaining_days_in_year:
                total_years += 1.0
                delta_days -= remaining_days_in_year
                current_year += 1
                start_date = date(current_year, 1, 1)
            else:
                total_years += delta_days / days_in_current_year
                break
                
        return total_years

if __name__ == '__main__':
    start = date(2000, 1, 1)
    end = date(2023, 12, 31)
    result = DateCalculator.calculate_years_between(start, end)
    print(result)