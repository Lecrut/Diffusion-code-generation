from datetime import datetime, timedelta

class DateUtils:
    @staticmethod
    def upcoming_monday():
        today = datetime.now()
        days_until_monday = (7 - today.weekday()) % 7
        return (today + timedelta(days=days_until_monday)).isoformat()

if __name__ == '__main__':
    print(DateUtils.upcoming_monday())