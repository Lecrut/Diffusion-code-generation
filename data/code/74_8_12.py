import datetime

class CurrentDayOfWeek:
    def __init__(self):
        self.now = datetime.datetime.now()

    def get_day_of_week(self):
        return self.now.strftime("%A")

if __name__ == '__main__':
    day_finder = CurrentDayOfWeek()
    print(day_finder.get_day_of_week())