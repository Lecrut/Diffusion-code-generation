import datetime

class DayOfWeekFetcher:
    DAY_NAMES = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    
    @staticmethod
    def get_current_day_name():
        return DayOfWeekFetcher.DAY_NAMES[datetime.date.today().weekday()]

if __name__ == '__main__':
    print(f"The current day of the week is: {DayOfWeekFetcher.get_current_day_name()}")