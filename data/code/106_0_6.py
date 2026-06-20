from datetime import datetime

class DateDifferenceCalculator:
    DATE_FORMAT = "%Y-%m-%d"

    @staticmethod
    def calculate_difference(date_str1, date_str2):
        date1 = datetime.strptime(date_str1, DateDifferenceCalculator.DATE_FORMAT)
        date2 = datetime.strptime(date_str2, DateDifferenceCalculator.DATE_FORMAT)
        difference = abs((date2 - date1).days) // 365
        return difference

if __name__ == '__main__':
    sample_date1 = "1990-05-15"
    sample_date2 = "2023-04-10"
    calculator = DateDifferenceCalculator()
    print(calculator.calculate_difference(sample_date1, sample_date2))