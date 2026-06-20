import datetime

class DayOfWeekFetcher:
    def __init__(self):
        self.current_day = datetime.datetime.now()

    def get_current_day_of_week(self):
        return self.current_day.strftime("%A")

if __name__ == '__main__':
    fetcher = DayOfWeekFetcher()
    print(fetcher.get_current_day_of_week())