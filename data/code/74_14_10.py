import datetime

class DayOfWeek:
    def __init__(self):
        self.today = datetime.datetime.now()

    def get_current_day_of_week(self):
        return self.today.strftime("%A")

if __name__ == '__main__':
    day_of_week_instance = DayOfWeek()
    print(day_of_week_instance.get_current_day_of_week())