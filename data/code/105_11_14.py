from datetime import datetime, timedelta

class DateHelper:

    def determine_next_date(self, days):
        today = datetime.now()
        days_until_monday = (7 - today.weekday()) % 7 + days
        return (today + timedelta(days=days_until_monday)).isoformat()
if __name__ == '__main__':
    helper = DateHelper()
    print(helper.determine_next_date(0))