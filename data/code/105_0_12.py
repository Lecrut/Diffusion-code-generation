import datetime

class DateUtil:
    def __init__(self):
        self.today = datetime.date.today()

    def get_next_monday(self):
        days_until_monday = (7 - self.today.weekday()) % 7
        return self.today + datetime.timedelta(days=days_until_monday)

if __name__ == '__main__':
    date_util = DateUtil()
    next_monday_date = date_util.get_next_monday()
    print(next_monday_date.strftime("%Y-%m-%d"))