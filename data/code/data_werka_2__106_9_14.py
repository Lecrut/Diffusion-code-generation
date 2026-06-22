from datetime import date

class DateCalculator:
    _MIN_YEAR = 1
    _MAX_YEAR = 9999

    @staticmethod
    def _is_birthday_passed(current: date, reference: date) -> bool:
        return (current.month, current.day) >= (reference.month, reference.day)

    @staticmethod
    def compute_year_difference(start: date, end: date) -> int:
        if not isinstance(start, date) or not isinstance(end, date):
            raise ValueError("Inputs must be date objects")
        
        if start.year < DateCalculator._MIN_YEAR or start.year > DateCalculator._MAX_YEAR:
            raise ValueError("Start year out of range")
        if end.year < DateCalculator._MIN_YEAR or end.year > DateCalculator._MAX_YEAR:
            raise ValueError("End year out of range")

        if start > end:
            return -DateCalculator.compute_year_difference(end, start)

        years_diff = end.year - start.year
        if not DateCalculator._is_birthday_passed(end, start):
            years_diff -= 1
        
        return years_diff

if __name__ == '__main__':
    start_date = date(1990, 2, 28)
    end_date = date(2024, 2, 27)
    calc = DateCalculator()
    diff = calc.compute_year_difference(start_date, end_date)
    print(diff)