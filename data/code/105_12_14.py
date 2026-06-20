from datetime import datetime, timedelta

class WeekdayFinder:
    def __init__(self):
        self.weekdays = {
            'Monday': 0,
            'Tuesday': 1,
            'Wednesday': 2,
            'Thursday': 3,
            'Friday': 4,
            'Saturday': 5,
            'Sunday': 6
        }

    def get_next_weekday(self, start_date_str, weekday):
        start_date = datetime.strptime(start_date_str, "%Y-%m-%d").date()
        target_day_index = self.weekdays[weekday]
        current_day_index = start_date.weekday()

        days_to_add = (target_day_index - current_day_index) % 7
        if days_to_add == 0:
            days_to_add = 7

        next_weekday_date = start_date + timedelta(days=days_to_add)
        return next_weekday_date.strftime("%Y-%m-%d")

if __name__ == '__main__':
    finder = WeekdayFinder()
    start_date = "2023-10-01"
    weekday = "Friday"
    result = finder.get_next_weekday(start_date, weekday)
    print(result)