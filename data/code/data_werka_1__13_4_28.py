from datetime import datetime
import pytz

class DateTimeNormalizer:
    def __init__(self):
        self.utc = pytz.utc

    def normalize_to_utc(self, time_str1, timezone1, time_str2, timezone2):
        tz1 = pytz.timezone(timezone1)
        tz2 = pytz.timezone(timezone2)

        dt1 = datetime.strptime(time_str1, '%Y-%m-%d %H:%M:%S')
        dt2 = datetime.strptime(time_str2, '%Y-%m-%d %H:%M:%S')

        dt1 = tz1.localize(dt1).astimezone(self.utc)
        dt2 = tz2.localize(dt2).astimezone(self.utc)

        return dt1, dt2

if __name__ == '__main__':
    normalizer = DateTimeNormalizer()
    time_str1 = '2023-10-01 12:00:00'
    timezone1 = 'America/New_York'
    time_str2 = '2023-10-01 15:00:00'
    timezone2 = 'Europe/London'

    utc_time1, utc_time2 = normalizer.normalize_to_utc(time_str1, timezone1, time_str2, timezone2)
    print(utc_time1)
    print(utc_time2)