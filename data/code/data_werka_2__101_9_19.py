import datetime
from datetime import datetime

class DayCalculator:
    DATE_PATTERN = "%Y-%m-%d"

    def __init__(self, date_string):
        self.date_string = date_string

    @staticmethod
    def parse(date_str):
        return datetime.strptime(date_str, DayCalculator.DATE_PATTERN)

    def get_weekday(self):
        dt = self.parse(self.date_string)
        return dt.strftime("%A").upper()

if __name__ == '__main__':
    calc = DayCalculator("2023-11-11")
    print(calc.get_weekday())