import calendar

class WeekdayChecker:
    WEEKDAY_NAMES = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
    
    @staticmethod
    def is_weekday(date_obj):
        return 0 <= date_obj.weekday() < len(WeekdayChecker.WEEKDAY_NAMES)

if __name__ == '__main__':
    sample_dt = datetime(2023, 10, 10)
    print(WeekdayChecker.is_weekday(sample_dt))