import datetime

class DayOfWeek:
    def __init__(self):
        self.days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    
    def get_current_day(self):
        today = datetime.date.today()
        day_index = today.weekday()
        return self.days_of_week[day_index]

if __name__ == '__main__':
    day_finder = DayOfWeek()
    current_day = day_finder.get_current_day()
    print(current_day)