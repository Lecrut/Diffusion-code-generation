from datetime import date

class YearDifferenceCalculator:
    EPOCH_YEAR = 1970
    
    @staticmethod
    def calculate_year_difference(date1: date, date2: date) -> int:
        return abs((date2 - date1).days // 365)

if __name__ == '__main__':
    sample_date1 = date(1980, 7, 4)
    sample_date2 = date(2023, 10, 11)
    calculator = YearDifferenceCalculator()
    print(calculator.calculate_year_difference(sample_date1, sample_date2))