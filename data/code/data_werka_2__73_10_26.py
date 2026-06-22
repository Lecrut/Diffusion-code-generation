import datetime

class TimeCalculator:
    DAYS_IN_WEEK = 7
    HOURS_IN_DAY = 24
    MINUTES_IN_HOUR = 60
    SECONDS_IN_MINUTE = 60
    SECONDS_IN_HOUR = 3600
    SECONDS_IN_DAY = 86400

    def _parse_time(self, time_input):
        if isinstance(time_input, datetime.datetime):
            return time_input
        if isinstance(time_input, str):
            return datetime.datetime.fromisoformat(time_input)
        raise ValueError("Unsupported time input type")

    def diff(self, start_time, end_time):
        start_dt = self._parse_time(start_time)
        end_dt = self._parse_time(end_time)
        delta = end_dt - start_dt
        total_seconds = int(delta.total_seconds())
        negative = total_seconds < 0
        abs_seconds = abs(total_seconds)
        days = abs_seconds // self.SECONDS_IN_DAY
        remaining = abs_seconds % self.SECONDS_IN_DAY
        hours = remaining // self.HOURS_IN_DAY
        remaining = remaining % self.HOURS_IN_DAY
        minutes = remaining // self.MINUTES_IN_HOUR
        seconds = remaining % self.MINUTES_IN_HOUR
        parts = []
        if days > 0:
            parts.append(f'{days} days')
        if hours > 0:
            parts.append(f'{hours} hours')
        if minutes > 0:
            parts.append(f'{minutes} minutes')
        if seconds > 0 or not parts:
            parts.append(f'{seconds} seconds')
        result = ', '.join(parts)
        if negative:
            result = f'-{result}'
        return result

if __name__ == '__main__':
    calculator = TimeCalculator()
    start = datetime.datetime(2023, 1, 1, 10, 0, 0)
    end = datetime.datetime(2023, 1, 3, 12, 30, 45)
    result = calculator.diff(start, end)
    print(result)
    start_str = "2023-01-01T10:00:00"
    end_str = "2023-01-03T12:30:45"
    result_str = calculator.diff(start_str, end_str)
    print(result_str)