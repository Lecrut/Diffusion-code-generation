from datetime import date, timedelta

class DateHelper:
    def __init__(self, target_date):
        self.target_date = target_date

    def get_next_monday(self):
        current_weekday = self.target_date.weekday()
        days_ahead = 7 - current_weekday
        if days_ahead == 7:
            days_ahead = 0
        return self.target_date + timedelta(days=days_ahead)

if __name__ == '__main__':
    helper = DateHelper(date(2023, 10, 1))
    result = helper.get_next_monday()
    print(result.isoformat())