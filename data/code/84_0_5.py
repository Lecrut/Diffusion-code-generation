class DateCalculator:
    MONTHS_DAYS = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    @staticmethod
    def is_leap_year(year):
        return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
    
    @classmethod
    def calculate_day_of_year(cls, year, month, day):
        if cls.is_leap_year(year):
            cls.MONTHS_DAYS[1] = 29
        return sum(cls.MONTHS_DAYS[:month - 1]) + day

if __name__ == '__main__':
    calculator = DateCalculator()
    print(calculator.calculate_day_of_year(2024, 2, 29))