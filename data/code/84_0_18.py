class DateCalculator:
    MONTHS = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    @staticmethod
    def is_leap_year(year):
        return (year % 4 == 0 and year % 100 != 0) or year % 400 == 0
    
    @classmethod
    def calculate_day_of_year(cls, year, month, day):
        if cls.is_leap_year(year):
            cls.MONTHS[1] = 29
        return sum(cls.MONTHS[:month - 1]) + day

if __name__ == '__main__':
    calculator = DateCalculator()
    result = calculator.calculate_day_of_year(2023, 4, 15)
    print(result)