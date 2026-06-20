from datetime import datetime

class DateDifferenceCalculator:
    def calculate_difference(self, date1_str, date2_str):
        date_format = "%Y-%m-%d"
        date1 = datetime.strptime(date1_str, date_format)
        date2 = datetime.strptime(date2_str, date_format)
        return abs((date2 - date1).days) // 365

if __name__ == '__main__':
    calculator = DateDifferenceCalculator()
    sample_date1 = "1990-05-15"
    sample_date2 = "2023-04-10"
    difference = calculator.calculate_difference(sample_date1, sample_date2)
    print(difference)