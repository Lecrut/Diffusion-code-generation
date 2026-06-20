from datetime import datetime

class DateCalculator:
    def calculate_difference(self, date1_str, date2_str):
        date_format = "%Y-%m-%d"
        date1 = datetime.strptime(date1_str, date_format)
        date2 = datetime.strptime(date2_str, date_format)
        difference = abs((date2 - date1).days)
        return difference

if __name__ == '__main__':
    calculator = DateCalculator()
    sample_date_a = "2023-01-05"
    sample_date_b = "2023-01-20"
    result = calculator.calculate_difference(sample_date_a, sample_date_b)
    print(result)