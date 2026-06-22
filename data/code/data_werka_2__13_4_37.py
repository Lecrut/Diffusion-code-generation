from datetime import datetime, timezone

class DateTimeNormalizer:
    def __init__(self, time1_str, time2_str):
        self.time1 = self._parse_time(time1_str)
        self.time2 = self._parse_time(time2_str)

    def _parse_time(self, time_str):
        try:
            if 'Z' in time_str or '+00:00' in time_str:
                naive_time = datetime.fromisoformat(time_str.replace('Z', '+00:00'))
            else:
                naive_time = datetime.fromisoformat(time_str)
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
    print('Normalized UTC Time 1:', utc_times[0])
    print('Normalized UTC Time 2:', utc_times[1])