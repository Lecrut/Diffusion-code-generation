from datetime import datetime, timedelta

class DateManipulator:
    def __init__(self, date):
        self.date = date

    def month_later(self):
        return self.date + timedelta(days=30)

if __name__ == '__main__':
    manipulator = DateManipulator(datetime(2023, 10, 15))
    print(manipulator.month_later())