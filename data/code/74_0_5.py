import datetime

class DayOfWeek:
    DAYS = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    
    @staticmethod
    def get_current_day_of_week():
        return DayOfWeek.DAYS[datetime.datetime.now().weekday()]

if __name__ == '__main__':
    print(DayOfWeek.get_current_day_of_week())