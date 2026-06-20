import datetime

class DayOfWeekFetcher:
    def __init__(self):
        self.current_date = datetime.datetime.now()

    def get_day_of_week(self):
        return self.current_date.strftime("%A")

if __name__ == '__main__':
    fetcher = DayOfWeekFetcher()
    print(fetcher.get_day_of_week())