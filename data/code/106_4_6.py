from datetime import date

class YearDifferenceCalculator:
    EPOCH_YEAR = 1970
    
    @staticmethod
    def years_difference(date1, date2):
        return abs((date2 - date1).days // 365)

if __name__ == '__main__':
    calculator = YearDifferenceCalculator()
    print(calculator.years_difference(date(2020, 1, 1), date(2023, 4, 1)))
    print(calculator.years_difference(date(2019, 12, 31), date(2020, 1, 1)))