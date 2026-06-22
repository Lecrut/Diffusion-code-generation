from datetime import datetime
import pytz

class TimeScaleManager:
    def convert_time(self, from_time_str, from_tz_str, to_tz_str):
        try:
            from_tz = pytz.timezone(from_tz_str)
            to_tz = pytz.timezone(to_tz_str)

            naive_from_time = datetime.fromisoformat(from_time_str)
            localized_from_time = from_tz.localize(naive_from_time)
            converted_to_time = localized_from_time.astimezone(to_tz)

            return converted_to_time.isoformat()
        except Exception as e:
            return str(e)

if __name__ == '__main__':
    manager = TimeScaleManager()
    from_time = "2023-10-15T14:00:00"
    from_timezone = "America/New_York"
    to_timezone = "Europe/London"

    converted_time = manager.convert_time(from_time, from_timezone, to_timezone)
    print(converted_time)