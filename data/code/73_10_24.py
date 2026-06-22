import datetime

class TimeCalculator:
    def diff(self, start_time, end_time):
        start = self._parse_time(start_time)
        end = self._parse_time(end_time)
        delta = end - start
        total_seconds = int(delta.total_seconds())
        if total_seconds < 0:
            total_seconds = -total_seconds
            sign = '-'
        else:
            sign = ''
        days = total_seconds // 86400
        remaining = total_seconds % 86400
        hours = remaining // 3600
        remaining = remaining % 3600
        minutes = remaining // 60
        seconds = remaining % 60
        parts = []
        if days > 0:
            parts.append(f"{days} day{'s' if days != 1 else ''}")
        if hours > 0:
            parts.append(f"{hours} hour{'s' if hours != 1 else ''}")
        if minutes > 0:
            parts.append(f"{minutes} minute{'s' if minutes != 1 else ''}")
        if seconds > 0 or not parts:
            parts.append(f"{seconds} second{'s' if seconds != 1 else ''}")
        return f"{sign}{', '.join(parts)}"

    def _parse_time(self, time_input):
        if isinstance(time_input, datetime.datetime):
            return time_input
        if isinstance(time_input, str):
            try:
                return datetime.datetime.fromisoformat(time_input)
            except ValueError:
                raise ValueError(f"Unsupported time format: {time_input}")
        raise ValueError(f"Unsupported input type: {type(time_input)}")

if __name__ == '__main__':
    calculator = TimeCalculator()
    start = datetime.datetime(2023, 10, 1, 10, 0, 0)
    end = datetime.datetime(2023, 10, 5, 14, 30, 45)
    result = calculator.diff(start, end)
    print(result)
    start_str = "2023-10-01T10:00:00"
    end_str = "2023-10-05T14:30:45"
    result_str = calculator.diff(start_str, end_str)
    print(result_str)