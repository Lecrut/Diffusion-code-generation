from datetime import datetime

class DateDifferenceCalculator:
    DATE_FORMAT = '%Y-%m-%d'
    
    @staticmethod
    def calculate_difference(date1_str, date2_str):
        date1 = datetime.strptime(date1_str, DateDifferenceCalculator.DATE_FORMAT)
        date2 = datetime.strptime(date2_str, DateDifferenceCalculator.DATE_FORMAT)
        return abs((date2 - date1).days)

if __name__ == '__main__':
    calculator = DateDifferenceCalculator()
    date1 = "2023-01-01"
    date2 = "2023-01-10"
    difference = calculator.calculate_difference(date1, date2)
    print(difference)