import datetime

class TimeCalculator:
    DAYS_IN_DAY = 86400
    HOURS_IN_DAY = 3600
    MINUTES_IN_HOUR = 60

    def diff(self, start_time, end_time):
        start_dt = self._parse(start_time)
        end_dt = self._parse(end_time)
        delta = end_dt - start_dt
        total_seconds = abs(int(delta.total_seconds()))
        
        days = total_seconds // self.DAYS_IN_DAY
        remaining = total_seconds % self.DAYS_IN_DAY
        hours = remaining // self.HOURS_IN_DAY
        remaining = remaining % self.HOURS_IN_DAY
        minutes = remaining // self.MINUTES_IN_HOUR
        seconds = remaining % self.MINUTES_IN_HOUR
        
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

    def _parse(self, time_input):
        if isinstance(time_input, datetime.datetime):
            return time_input
        if isinstance(time_input, str):
            return datetime.datetime.fromisoformat(time_input)
        raise ValueError(f"Unsupported type: {type(time_input)}")

if __name__ == '__main__':
    calc = TimeCalculator()
    start = datetime.datetime(2023, 1, 1, 10, 0, 0)
    end = datetime.datetime(2023, 1, 3, 14, 30, 45)
    result = calc.diff(start, end)
    print(result)