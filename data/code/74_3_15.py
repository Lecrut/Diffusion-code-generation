from datetime import datetime

class WeekdayFetcher:
    DAY_FORMAT = '%A'

    @staticmethod
    def get_current_day():
        return datetime.now().strftime(WeekdayFetcher.DAY_FORMAT)

if __name__ == '__main__':
    print(WeekdayFetcher.get_current_day())