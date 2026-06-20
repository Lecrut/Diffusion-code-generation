from datetime import datetime, timedelta

class DateHandler:
    def get_next_monday(self):
        today = datetime.now()
        days_until_monday = (7 - today.weekday()) % 7
        next_monday = today + timedelta(days=days_until_monday)
        return next_monday.isoformat()

if __name__ == '__main__':
    handler = DateHandler()
    print(handler.get_next_monday())