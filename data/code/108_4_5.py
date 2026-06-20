import calendar

class DateHandler:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day
    
    def get_day_of_week(self):
        return calendar.monthrange(self.year, self.month)[1]

if __name__ == '__main__':
    handler = DateHandler(2023, 10, 15)
    print(f"Day {handler.day} of Month {handler.month} in the year {handler.year} falls on day number: {handler.get_day_of_week()}")