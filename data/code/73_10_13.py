import datetime

class TimeCalculator:
    DAYS_IN_DAY = 86400
    HOURS_IN_DAY = 3600
    MINUTES_IN_HOUR = 60
    SECONDS_IN_MINUTE = 1

    def _parse_input(self, time_input):
        if isinstance(time_input, datetime.datetime):
            return time_input
        if isinstance(time_input, str):
            return datetime.datetime.fromisoformat(time_input)
        raise ValueError(f"Unsupported time type: {type(time_input)}")

    def diff(self, start_time, end_time):
        start_dt = self._parse_input(start_time)
        end_dt = self._parse_input(end_time)
        delta = end_dt - start_dt
        total_seconds = int(abs(delta.total_seconds()))
        days = total_seconds // self.DAYS_IN_DAY
        remaining_seconds = total_seconds % self.DAYS_IN_DAY
        hours = remaining_seconds // self.HOURS_IN_DAY
        remaining_seconds = remaining_seconds % self.HOURS_IN_DAY
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
        return ", ".join(parts)

if __name__ == '__main__':
    calculator = TimeCalculator()
    start = datetime.datetime(2023, 1, 1, 10, 0, 0)
    end = datetime.datetime(2023, 1, 3, 12, 30, 45)
    result = calculator.diff(start, end)
    print(result)
    start_str = "2023-01-01T10:00:00"
    end_str = "2023-01-02T11:15:30"
    result_str = calculator.diff(start_str, end_str)
    print(result_str)