class DateCalculator:
    def get_day_of_year(self, year, month, day):
        if not (1 <= month <= 12) or not (1 <= day <= 31):
            raise ValueError("Invalid month or day")
        
        days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
            days_in_month[2] = 29
        
        if day > days_in_month[month]:
            raise ValueError("Day out of range for the given month and year")
        
        return sum(days_in_month[:month]) + day

if __name__ == '__main__':
    calculator = DateCalculator()
    sample_year = 2023
    sample_month = 10
    sample_day = 27
    print(calculator.get_day_of_year(sample_year, sample_month, sample_day))