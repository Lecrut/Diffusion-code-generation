from datetime import date
import calendar

class DateCalculator:
    REFERENCE_DATE = date(2023, 3, 3)
    TARGET_DAY = 15

    @staticmethod
    def _get_next_month(year: int, month: int) -> tuple:
        if month == 12:
            return year + 1, 1
        return year, month + 1

    @classmethod
    def find_next_15th(cls) -> date:
        ref = cls.REFERENCE_DATE
        year = ref.year
        month = ref.month
        
        if ref.day <= cls.TARGET_DAY:
            target_month = month
            target_year = year
        else:
            target_year, target_month = cls._get_next_month(year, month)
        
        return date(target_year, target_month, cls.TARGET_DAY)

if __name__ == '__main__':
    calc = DateCalculator()
    result = calc.find_next_15th()
    print(result)