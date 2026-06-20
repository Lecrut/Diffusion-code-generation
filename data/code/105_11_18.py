from datetime import datetime, timedelta

class DateHelper:
    @staticmethod
    def get_upcoming_monday():
        today = datetime.now()
        days_until_monday = (7 - today.weekday()) % 7
        upcoming_monday = today + timedelta(days=days_until_monday)
        return upcoming_monday.isoformat()

if __name__ == '__main__':
    helper_instance = DateHelper()
    print(helper_instance.get_upcoming_monday())