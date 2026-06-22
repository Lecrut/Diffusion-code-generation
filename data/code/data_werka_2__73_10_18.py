import datetime

class TimeCalculator:
    _DAY_SECONDS = 86400
    _HOUR_SECONDS = 3600
    _MINUTE_SECONDS = 60

    def _parse_time(self, time_input):
        if isinstance(time_input, datetime.datetime):
            return time_input
        if isinstance(time_input, str):
            return datetime.datetime.fromisoformat(time_input)
        raise ValueError("Unsupported time type")

    def diff(self, start_time, end_time):
        start = self._parse_time(start_time)
        end = self._parse_time(end_time)
        delta = end - start
        total_seconds = abs(int(delta.total_seconds()))
        
        days = total_seconds // self._DAY_SECONDS
        remaining = total_seconds % self._DAY_SECONDS
        hours = remaining // self._HOUR_SECONDS
        remaining = remaining % self._HOUR_SECONDS
        minutes = remaining // self._MINUTE_SECONDS
        seconds = remaining % self._MINUTE_SECONDS
        
        parts = []
        if days > 0:
            parts.append(f'{days} days')
        if hours > 0:
            parts.append(f'{hours} hours')
        if minutes > 0:
            parts.append(f'{minutes} minutes')
        if seconds > 0:
            parts.append(f'{seconds} seconds')
            
        if not parts:
            return '0 seconds'
        return ', '.join(parts)

if __name__ == '__main__':
    calculator = TimeCalculator()
    start = datetime.datetime(2023, 10, 1, 10, 0, 0)
    end = datetime.datetime(2023, 10, 5, 14, 30, 45)
    result = calculator.diff(start, end)
    print(result)