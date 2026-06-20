from datetime import datetime

class DateCalculator:
    def calculate_difference(self, date1_str, date2_str):
        date_format = "%Y-%m-%d"
        date1 = datetime.strptime(date1_str, date_format)
        date2 = datetime.strptime(date2_str, date_format)
        return abs((date2 - date1).days)

if __name__ == '__main__':
    calculator = DateCalculator()
    start_date = "2023-02-01"
    end_date = "2023-02-28"
    diff_days = calculator.calculate_difference(start_date, end_date)
    print(diff_days)