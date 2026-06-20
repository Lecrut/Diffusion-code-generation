from datetime import datetime

class DayOfWeekFetcher:
    DAY_FORMAT = '%A'

    @staticmethod
    def get_current_day():
        return datetime.now().strftime(DayFormatter.DAY_FORMAT)

if __name__ == '__main__':
    print(DayOfWeekFetcher.get_current_day())