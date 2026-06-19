from datetime import datetime
import pytz

class DateTimeNormalizer:

    def __init__(self, time1, time2):
        self.time1 = self._normalize_to_utc(time1)
        self.time2 = self._normalize_to_utc(time2)

    def _normalize_to_utc(self, time_str):
        try:
            naive_time = datetime.fromisoformat(time_str.replace('Z', '+00:00'))
            if naive_time.tzinfo is not None:
                return naive_time.astimezone(pytz.utc)
            else:
                local_tz = pytz.timezone('UTC')
                localized_time = local_tz.localize(naive_time)
                return localized_time.astimezone(pytz.utc)
        except Exception as e:
            raise ValueError(f'Invalid time format: {time_str}') from e

    def get_utc_times(self):
        return (self.time1, self.time2)
if __name__ == '__main__':
    time1 = '2023-10-05T14:48:00Z'
    time2 = '2023-10-05T09:30:00-05:00'
    normalizer = DateTimeNormalizer(time1, time2)
    utc_time1, utc_time2 = normalizer.get_utc_times()
    print(utc_time1)
    print(utc_time2)