import datetime

class DayOfWeekDisplay:
    def get_current_day_of_week(self):
        return datetime.datetime.now().strftime("%A")

if __name__ == '__main__':
    display = DayOfWeekDisplay()
    day_name = display.get_current_day_of_week()
    print(day_name)