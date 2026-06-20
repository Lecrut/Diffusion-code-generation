from datetime import datetime

class WeekdayFetcher:
    def get_current_day(self):
        return datetime.now().strftime('%A')

if __name__ == '__main__':
    fetcher = WeekdayFetcher()
    print("Today is:", fetcher.get_current_day())