from datetime import datetime
import pytz

class TimeScaleManager:
    def convert_time(self, time_str, from_tz, to_tz):
        naive_datetime = datetime.strptime(time_str, '%Y-%m-%d %H:%M:%S')
        from_timezone = pytz.timezone(from_tz)
        to_timezone = pytz.timezone(to_tz)
        
        localized_datetime = from_timezone.localize(naive_datetime)
        converted_datetime = localized_datetime.astimezone(to_timezone)
        
        return converted_datetime.strftime('%Y-%m-%d %H:%M:%S')

if __name__ == '__main__':
    manager = TimeScaleManager()
    time_str = '2023-10-15 14:00:00'
    from_tz = 'America/New_York'
    to_tz = 'Europe/London'
    
    converted_time = manager.convert_time(time_str, from_tz, to_tz)
    print(converted_time)