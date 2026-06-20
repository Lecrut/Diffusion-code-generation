import datetime

class TimeCalculator:
    def diff(self, start_time, end_time):
        if isinstance(start_time, str):
            start_time = self._parse_iso_format(start_time)
        if isinstance(end_time, str):
            end_time = self._parse_iso_format(end_time)
        
        delta = abs(end_time - start_time)
        days = delta.days
        hours = (delta.seconds // 3600) % 24
        
        return f'{days} days, {hours} hours'

    def _parse_iso_format(self, time_str):
        try:
            return datetime.datetime.fromisoformat(time_str)
        except ValueError:
            raise ValueError("Invalid ISO format")

if __name__ == '__main__':
    calculator = TimeCalculator()
    result = calculator.diff('2023-10-01T00:00:00', '2023-10-05T12:00:00')
    print(result)