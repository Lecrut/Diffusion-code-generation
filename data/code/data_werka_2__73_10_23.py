import datetime

class TimeCalculator:
    DAYS_IN_HOUR = 24
    HOURS_IN_DAY = 24
    MINUTES_IN_HOUR = 60
    SECONDS_IN_MINUTE = 60
    SECONDS_IN_HOUR = 3600
    SECONDS_IN_DAY = 86400

    def diff(self, start_time, end_time):
        start_dt = self._parse_time(start_time)
        end_dt = self._parse_time(end_time)
        delta = end_dt - start_dt
        total_seconds = int(delta.total_seconds())
        if total_seconds < 0:
            sign = "-"
            total_seconds = -total_seconds
        else:
            sign = ""
        days = total_seconds // self.SECONDS_IN_DAY
        remaining_seconds = total_seconds % self.SECONDS_IN_DAY
        hours = remaining_seconds // self.SECONDS_IN_HOUR
        remaining_seconds = remaining_seconds % self.SECONDS_IN_HOUR
        minutes = remaining_seconds // self.MINUTES_IN_HOUR
        seconds = remaining_seconds % self.MINUTES_IN_HOUR
        parts = []
        if days > 0:
            parts.append(f"{days} days")
        if hours > 0:
            parts.append(f"{hours} hours")
        if minutes > 0:
            parts.append(f"{minutes} minutes")
        if seconds > 0 or not parts:
            parts.append(f"{seconds} seconds")
        result = ", ".join(parts)
        return f"{sign}{result}"

    def _parse_time(self, time_input):
        if isinstance(time_input, datetime.datetime):
            return time_input
        if isinstance(time_input, str):
            return datetime.datetime.fromisoformat(time_input)
        raise ValueError("Unsupported time input type")

if __name__ == '__main__':
    calculator = TimeCalculator()
    start = datetime.datetime(2023, 1, 1, 10, 0, 0)
    end = datetime.datetime(2023, 1, 5, 14, 30, 45)
    result = calculator.diff(start, end)
    print(result)
    result2 = calculator.diff("2023-01-01T10:00:00", "2023-01-01T12:05:10")
    print(result2)