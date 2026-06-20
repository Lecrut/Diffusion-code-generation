from datetime import datetime, timedelta

class DateHandler:
    WEEKDAY_MONDAY = 0
    
    def find_next_monday(self):
        today = datetime.now()
        days_until_monday = (self.WEEKDAY_MONDAY - today.weekday() + 7) % 7
        next_monday = today + timedelta(days=days_until_monday)
        return next_monday.isoformat()

if __name__ == '__main__':
    date_handler = DateHandler()
    print(date_handler.find_next_monday())