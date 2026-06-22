from datetime import datetime, timezone

class DateTimeNormalizer:
    def __init__(self, time_str1, time_str2):
        self.time1 = self._parse_time(time_str1)
        self.time2 = self._parse_time(time_str2)

    def _parse_time(self, time_str):
        try:
            naive_time = datetime.fromisoformat(time_str.replace('Z', '+00:00'))
            return naive_time.astimezone(timezone.utc)
        except ValueError as e:
            raise ValueError(f'Invalid time format: {e}')

    def normalize_times(self):
        return (self.time1, self.time2)

if __name__ == '__main__':
    time_str1 = '2023-10-05T14:48:00Z'
    time_str2 = '2023-10-05T09:30:00-05:00'
    normalizer = DateTimeNormalizer(time_str1, time_str2)
    utc_times = normalizer.normalize_times()
    print('UTC Time 1:', utc_times[0])
    print('UTC Time 2:', utc_times[1])