import datetime

class DayOfWeek:
    def __init__(self):
        self.current_day = datetime.datetime.now().strftime("%A")

    def get_current_day(self):
        return self.current_day

if __name__ == '__main__':
    day_instance = DayOfWeek()
    print(day_instance.get_current_day())