import datetime

class TimeCalculator:
    def diff(self, start_time, end_time):
        start = self._parse_time(start_time)
        end = self._parse_time(end_time)
        delta = end - start
        total_seconds = int(delta.total_seconds())
        if total_seconds < 0:
            total_seconds = -total_seconds
        days = total_seconds // 86400
        remaining = total_seconds % 86400
        hours = remaining // 3600
        remaining = remaining % 3600
        minutes = remaining // 60
        seconds = remaining % 60
        parts = []
        if days > 0:
            parts.append(f'{days} days')
        if hours > 0:
            parts.append(f'{hours} hours')
        if minutes > 0:
            parts.append(f'{minutes} minutes')
        if seconds > 0 or not parts:
            parts.append(f'{seconds} seconds')
        return ', '.join(parts)

    def _parse_time(self, time_input):
        if isinstance(time_input, datetime.datetime):
            return time_input
        if isinstance(time_input, str):
            return datetime.datetime.fromisoformat(time_input)
        raise ValueError("Unsupported time type")

if __name__ == '__main__':
    calculator = TimeCalculator()
    start = datetime.datetime(2023, 1, 1, 10, 0, 0)
    end = datetime.datetime(2023, 1, 3, 12, 30, 45)
    result = calculator.diff(start, end)
    print(result)
    result2 = calculator.diff("2023-01-01T10:00:00", "2023-01-02T11:00:00")
    print(result2)