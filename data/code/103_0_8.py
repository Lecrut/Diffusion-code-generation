import datetime

class MidnightTimer:
    SECONDS_IN_HOUR = 3600
    SECONDS_IN_DAY = 86400

    @staticmethod
    def _get_start_of_day(dt):
        return dt.replace(hour=0, minute=0, second=0, microsecond=0)

    @classmethod
    def calculate_elapsed_seconds(cls):
        now = datetime.datetime.now()
        start = cls._get_start_of_day(now)
        delta = now - start
        return delta.total_seconds()

if __name__ == '__main__':
    value = MidnightTimer.calculate_elapsed_seconds()
    print(value)