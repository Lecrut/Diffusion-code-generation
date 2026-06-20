from datetime import datetime, timedelta

class DateHandler:
    def __init__(self, target_date_str):
        self.target_date = datetime.strptime(target_date_str, "%Y-%m-%d")

    def find_next_wednesday(self):
        days_until_wednesday = (2 - self.target_date.weekday()) % 7
        next_wednesday = self.target_date + timedelta(days=days_until_wednesday)
        return next_wednesday

if __name__ == '__main__':
    handler = DateHandler("2023-10-10")
    next_wednesday = handler.find_next_wednesday()
    print(next_wednesday.strftime("%Y-%m-%d"))