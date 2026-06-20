from datetime import datetime

class WeekdayFetcher:
    DAYS = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    @staticmethod
    def get_current_day():
        return WeekdayFetcher.DAYS[datetime.now().weekday()]

if __name__ == '__main__':
    fetcher = WeekdayFetcher()
    print(fetcher.get_current_day())