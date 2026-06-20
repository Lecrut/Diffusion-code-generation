import datetime

class DayOfWeek:
    def __init__(self):
        self.now = datetime.datetime.now()

    def get_day_of_week(self):
        return self.now.strftime("%A")

if __name__ == '__main__':
    day_of_week_instance = DayOfWeek()
    print(day_of_week_instance.get_day_of_week())