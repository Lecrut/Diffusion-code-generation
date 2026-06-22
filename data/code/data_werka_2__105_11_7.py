from datetime import date, timedelta

class NextMonday:
    def __init__(self, start_date=None):
        self.start_date = start_date if start_date is not None else date.today()

    def calculate(self):
        days_until_monday = (7 - self.start_date.weekday()) % 7
        if days_until_monday == 0:
            days_until_monday = 7
        return self.start_date + timedelta(days=days_until_monday)

if __name__ == '__main__':
    instance = NextMonday()
    print(instance.calculate().isoformat())