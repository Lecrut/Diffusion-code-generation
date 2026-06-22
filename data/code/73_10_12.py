import datetime

class TimeCalculator:
    SECONDS_PER_DAY = 86400
    SECONDS_PER_HOUR = 3600
    SECONDS_PER_MINUTE = 60

    def _parse_time(self, time_input):
        if isinstance(time_input, str):
            return datetime.datetime.fromisoformat(time_input)
        if isinstance(time_input, datetime.datetime):
            return time_input
        raise ValueError(f"Unsupported time type: {type(time_input)}")

    def diff(self, start_time, end_time):
        start_dt = self._parse_time(start_time)
        end_dt = self._parse_time(end_time)
        delta = end_dt - start_dt
        total_seconds = abs(int(delta.total_seconds()))
        days = total_seconds // self.SECONDS_PER_DAY
        remaining_seconds = total_seconds % self.SECONDS_PER_DAY
        hours = remaining_seconds // self.SECONDS_PER_HOUR
        remaining_seconds = remaining_seconds % self.SECONDS_PER_HOUR
        minutes = remaining_seconds // self.SECONDS_PER_MINUTE
        seconds = remaining_seconds % self.SECONDS_PER_MINUTE
        parts = []
        if days > 0:
            parts.append(f"{days} days")
        if hours > 0:
            parts.append(f"{hours} hours")
        if minutes > 0:
            parts.append(f"{minutes} minutes")
        if seconds > 0:
            parts.append(f"{seconds} seconds")
        if not parts:
            return "0 seconds"
        return ", ".join(parts)

if __name__ == '__main__':
    calculator = TimeCalculator()
    start = datetime.datetime(2023, 1, 1, 10, 0, 0)
    end = datetime.datetime(2023, 1, 3, 14, 30, 45)
    result = calculator.diff(start, end)
    print(result)
    iso_start = "2023-01-01T10:00:00"
    iso_end = "2023-01-02T12:00:00"
    result2 = calculator.diff(iso_start, iso_end)
    print(result2)