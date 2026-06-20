import datetime

class DayOfWeekFormatter:
    DAYS_OF_WEEK = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    
    @staticmethod
    def get_current_day_name():
        today = datetime.date.today()
        day_index = today.weekday()
        return DayOfWeekFormatter.DAYS_OF_WEEK[day_index]

if __name__ == '__main__':
    current_day_name = DayOfWeekFormatter.get_current_day_name()
    print(f"The current day of the week is: {current_day_name}")