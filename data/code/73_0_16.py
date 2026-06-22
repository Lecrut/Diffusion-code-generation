import datetime
import pytz

class TimeDeltaCalculator:

    def __init__(self, dt1, dt2):
        self.dt1 = self._ensure_tz(dt1)
        self.dt2 = self._ensure_tz(dt2)

    def _ensure_tz(self, dt):
        if dt.tzinfo is None:
            raise ValueError('Datetimes must be timezone aware.')
        return dt

    def get_difference(self):
        dt1_utc = self.dt1.astimezone(pytz.utc)
        dt2_utc = self.dt2.astimezone(pytz.utc)
        return dt2_utc - dt1_utc

    def get_seconds(self):
        diff = self.get_difference()
        return diff.total_seconds()

    def get_formatted_string(self):
        diff = self.get_difference()
        days = diff.days
        seconds = diff.seconds
        hours, remainder = divmod(seconds, 3600)
        minutes, secs = divmod(remainder, 60)
        return f'{days} days, {hours} hours, {minutes} minutes, {secs} seconds'
if __name__ == '__main__':
    tz_tokyo = pytz.timezone('Asia/Tokyo')
    tz_london = pytz.timezone('Europe/London')
    dt_tokyo = datetime.datetime(2023, 10, 26, 10, 0, 0, tzinfo=tz_tokyo)
    dt_london = datetime.datetime(2023, 10, 26, 10, 0, 0, tzinfo=tz_london)
    calc = TimeDeltaCalculator(dt_tokyo, dt_london)
    diff = calc.get_difference()
    seconds = calc.get_seconds()
    formatted = calc.get_formatted_string()
    print(f'Tokyo: {dt_tokyo}')
    print(f'London: {dt_london}')
    print(f'Difference (timedelta): {diff}')
    print(f'Difference (seconds): {seconds}')
    print(f'Difference (formatted): {formatted}')
    dt_tokyo_2 = datetime.datetime(2023, 10, 27, 10, 0, 0, tzinfo=tz_tokyo)
    dt_london_2 = datetime.datetime(2023, 10, 25, 10, 0, 0, tzinfo=tz_london)
    calc2 = TimeDeltaCalculator(dt_tokyo_2, dt_london_2)
    print(f'\nTokyo 2: {dt_tokyo_2}')
    print(f'London 2: {dt_london_2}')
    print(f'Difference (timedelta): {calc2.get_difference()}')
    print(f'Difference (formatted): {calc2.get_formatted_string()}')