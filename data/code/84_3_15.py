from datetime import datetime

class DateParser:
    MONTH_DAYS = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    @staticmethod
    def is_leap_year(year):
        return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
    
    @classmethod
    def day_of_year(cls, date_str):
        try:
            year, month, day = map(int, date_str.split('-'))
            if not (1 <= month <= 12 and 1 <= day <= cls.MONTH_DAYS[month]):
                raise ValueError("Invalid date")
            return sum(cls.MONTH_DAYS[:month]) + day + (cls.is_leap_year(year) and month > 2)
        except ValueError as e:
            print(f"Error: {e}")
            return None

if __name__ == '__main__':
    parser = DateParser()
    print(parser.day_of_year('2023-10-27'))