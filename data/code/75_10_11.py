import datetime

class DateCalculator:
    def calculate_difference(self, date1_str, date2_str):
        date_format = "%Y-%m-%d"
        date1 = datetime.datetime.strptime(date1_str, date_format)
        date2 = datetime.datetime.strptime(date2_str, date_format)
        return abs(date2 - date1)

if __name__ == '__main__':
    calculator = DateCalculator()
    difference = calculator.calculate_difference('2023-04-01', '2023-05-15')
    print(difference.days)