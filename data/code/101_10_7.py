import calendar

class DateAnalyzer:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day
    
    def get_day_of_week(self):
        return calendar.day_name[calendar.weekday(self.year, self.month, self.day)]

if __name__ == '__main__':
    sample_date = DateAnalyzer(2023, 12, 25)
    print(f"The day of the week for {sample_date.month}/{sample_date.year} is {sample_date.get_day_of_week()}.")