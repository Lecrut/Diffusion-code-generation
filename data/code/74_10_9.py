from datetime import datetime

class DayOfWeek:
    DAYS = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    
    def get_current_day(self):
        return self.DAYS[datetime.now().weekday()]

if __name__ == '__main__':
    day_of_week_instance = DayOfWeek()
    print(day_of_week_instance.get_current_day())