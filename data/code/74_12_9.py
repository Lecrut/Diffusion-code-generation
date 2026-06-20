import datetime

class DayOfWeekFormatter:
    DAYS = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    
    @staticmethod
    def get_current_day_name():
        today = datetime.date.today()
        day_index = today.weekday()
        return DayOfWeekFormatter.DAYS[day_index]

if __name__ == '__main__':
    print(f"The current day of the week is: {DayOfWeekFormatter.get_current_day_name()}")