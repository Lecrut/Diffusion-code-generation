from datetime import datetime

class DateDifferenceCalculator:
    DAYS_PER_WEEK = 7
    
    @staticmethod
    def calculate_week_difference(date_str1, date_str2):
        date_format = '%Y-%m-%d'
        date1 = datetime.strptime(date_str1, date_format)
        date2 = datetime.strptime(date_str2, date_format)
        difference = abs((date2 - date1).days)
        weeks = difference / DateDifferenceCalculator.DAYS_PER_WEEK
        return weeks

if __name__ == '__main__':
    calculator = DateDifferenceCalculator()
    result = calculator.calculate_week_difference("2023-01-01", "2023-01-29")
    print(f"The difference between the dates is approximately {result:.2f} weeks.")