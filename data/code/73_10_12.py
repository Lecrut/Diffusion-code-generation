from datetime import datetime

class DateDifferenceCalculator:
    @staticmethod
    def calculate_days_between(date_str1, date_str2):
        dt1 = datetime.strptime(date_str1, '%Y-%m-%d')
        dt2 = datetime.strptime(date_str2, '%Y-%m-%d')
        return abs((dt2 - dt1).days)

if __name__ == '__main__':
    calculator = DateDifferenceCalculator()
    difference1 = calculator.calculate_days_between('2023-01-01', '2023-01-03')
    print(f"Difference between 2023-01-01 and 2023-01-03: {difference1} days")
    
    difference2 = calculator.calculate_days_between('2023-01-10', '2023-01-10')
    print(f"Difference between 2023-01-10 and 2023-01-10: {difference2} days")
    
    difference3 = calculator.calculate_days_between('2023-01-05', '2023-01-01')
    print(f"Difference between 2023-01-05 and 2023-01-01: {difference3} days")