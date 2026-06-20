import datetime

class DayOfWeek:
    def __init__(self):
        self.now = datetime.datetime.now()

    def get_current_day_of_week(self):
        return self.now.strftime("%A")

if __name__ == '__main__':
    day = DayOfWeek()
    print(day.get_current_day_of_week())