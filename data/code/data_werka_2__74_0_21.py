import datetime

class WeekdayCalculator:
    def __init__(self, reference_date=None):
        if reference_date is not None:
            if not isinstance(reference_date, datetime.date):
                raise ValueError("reference_date must be a datetime.date instance")
            self.reference_date = reference_date
        else:
            self.reference_date = datetime.date.today()

    def get_name(self):
        return self.reference_date.strftime("%A")

    def get_short_name(self):
        return self.reference_date.strftime("%a")

    def get_numeric_index(self):
        return self.reference_date.weekday()

def calculate_weekday_details():
    calculator = WeekdayCalculator()
    return calculator

if __name__ == '__main__':
    calc = calculate_weekday_details()
    print(calc.get_name())