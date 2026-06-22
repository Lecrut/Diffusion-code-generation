import datetime

class WeekdayCalculator:
    FORMAT_UPPER = "%A"

    def __init__(self, year, month, day):
        self.date_obj = datetime.date(year, month, day)

    def get_weekday(self):
        return self.date_obj.strftime(self.FORMAT_UPPER).upper()

def compute_weekday(year, month, day):
    calculator = WeekdayCalculator(year, month, day)
    return calculator.get_weekday()

if __name__ == '__main__':
    result = compute_weekday(2024, 7, 4)
    print(result)