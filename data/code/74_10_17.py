from datetime import datetime

class CurrentDay:
    def __init__(self):
        self.days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    def get_current_day(self):
        current_day_index = datetime.now().weekday()
        return self.days_of_week[current_day_index]

if __name__ == '__main__':
    day_instance = CurrentDay()
    print(day_instance.get_current_day())