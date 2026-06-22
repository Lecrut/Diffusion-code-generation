import datetime

class TimeCalculator:
    def diff(self, start_time, end_time):
        start_dt = self._parse(start_time)
        end_dt = self._parse(end_time)
        delta = end_dt - start_dt
        total_seconds = abs(int(delta.total_seconds()))
        days = total_seconds // 86400
        remainder = total_seconds % 86400
        hours = remainder // 3600
        remainder = remainder % 3600
        minutes = remainder // 60
        seconds = remainder % 60
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

    def _parse(self, time_input):
        if isinstance(time_input, datetime.datetime):
            return time_input
        if isinstance(time_input, str):
            return datetime.datetime.fromisoformat(time_input)
        raise ValueError(f"Unsupported time type: {type(time_input)}")

if __name__ == '__main__':
    calculator = TimeCalculator()
    start = datetime.datetime(2023, 1, 1, 10, 0, 0)
    end = datetime.datetime(2023, 1, 3, 12, 30, 45)
    result = calculator.diff(start, end)
    print(result)