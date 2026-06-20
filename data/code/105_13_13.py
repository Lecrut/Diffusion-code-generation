import datetime

class DateFinder:
    def __init__(self):
        self.today = datetime.date.today()

    def find_next_weekend(self):
        days_ahead = 0
        while (self.today + datetime.timedelta(days=days_ahead)).weekday() < 5:
            days_ahead += 1
        return self.today + datetime.timedelta(days=days_ahead)

if __name__ == '__main__':
    finder = DateFinder()
    next_weekend = finder.find_next_weekend()
    print(f"Next Weekend: {next_weekend}")