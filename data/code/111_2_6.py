import datetime

class DateProcessor:
    def __init__(self):
        self.day_of_week_cache = {}

    def get_day_of_week(self, year, month, day):
        date_key = (year, month, day)
        if date_key in self.day_of_week_cache:
            return self.day_of_week_cache[date_key]
        
        date = datetime.date(year, month, day)
        day_of_week = date.strftime('%A')
        self.day_of_week_cache[date_key] = day_of_week
        return day_of_week

if __name__ == '__main__':
    processor = DateProcessor()
    print(processor.get_day_of_week(2024, 2, 29))