import datetime

class DateDifferenceCalculator:
    def __init__(self, date1_str, date2_str):
        self.date1 = datetime.datetime.strptime(date1_str, '%Y-%m-%d')
        self.date2 = datetime.datetime.strptime(date2_str, '%Y-%m-%d')

    def calculate_difference_in_weeks(self):
        time_difference = abs((self.date1 - self.date2).days)
        difference_in_weeks = time_difference / 7
        return difference_in_weeks

if __name__ == '__main__':
    calculator = DateDifferenceCalculator("2023-01-01", "2023-01-29")
    result = calculator.calculate_difference_in_weeks()
    print(result)