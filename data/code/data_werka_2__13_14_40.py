from datetime import datetime
import pytz

def validate_timezone(timezone_str):
    try:
        pytz.timezone(timezone_str)
    except pytz.UnknownTimeZoneError:
        raise ValueError(f"Invalid timezone: {timezone_str}")

class TimezoneConverter:
    def __init__(self, from_tz, to_tz):
        self.from_timezone = self._get_timezone(from_tz)
        self.to_timezone = self._get_timezone(to_tz)

    def _get_timezone(self, timezone_str):
        validate_timezone(timezone_str)
        return pytz.timezone(timezone_str)

    def convert(self, timestamp):
        naive_datetime = datetime.fromisoformat(timestamp)
        localized_datetime = self.from_timezone.localize(naive_datetime)
        converted_datetime = localized_datetime.astimezone(self.to_timezone)
        return converted_datetime.isoformat()

def batch_convert_timezones(timestamps, converter):
    converted_times = []
    for timestamp in timestamps:
        try:
            converted_time = converter.convert(timestamp)
            converted_times.append(converted_time)
        except (ValueError, pytz.UnknownTimeZoneError) as e:
            print(f"Failed to convert {timestamp}: {e}")
    return converted_times

if __name__ == '__main__':
    sample_timestamps = [
        '2023-10-01T12:00:00',
        '2023-10-02T15:30:00',
        '2023-10-03T09:45:00'
    ]
    converter = TimezoneConverter('UTC', 'America/New_York')
    converted_times = batch_convert_timezones(sample_timestamps, converter)
    for time in converted_times:
        print(time)