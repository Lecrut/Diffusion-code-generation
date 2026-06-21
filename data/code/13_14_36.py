from datetime import datetime
import pytz

class TimezoneConverter:
    def __init__(self, from_tz, to_tz):
        self.from_timezone = self._get_timezone(from_tz)
        self.to_timezone = self._get_timezone(to_tz)

    def _get_timezone(self, timezone_str):
        try:
            return pytz.timezone(timezone_str)
        except pytz.UnknownTimeZoneError:
            raise ValueError(f"Invalid timezone: {timezone_str}")

    def convert(self, timestamp):
        naive_datetime = datetime.fromisoformat(timestamp)
        localized_datetime = self.from_timezone.localize(naive_datetime)
        converted_datetime = localized_datetime.astimezone(self.to_timezone)
        return converted_datetime.isoformat()

def batch_convert_timezones(timestamps, converter):
    return [converter.convert(ts) for ts in timestamps]

if __name__ == '__main__':
    sample_timestamps = [
        '2023-10-01T12:00:00',
        '2023-10-02T15:30:00',
        '2023-10-03T09:45:00'
    ]

    converter = TimezoneConverter('UTC', 'America/New_York')
    converted_times = batch_convert_timezones(sample_timestamps, converter)

    for original, converted in zip(sample_timestamps, converted_times):
        print(f"Original: {original} -> Converted: {converted}")