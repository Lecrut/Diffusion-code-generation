import datetime

class TimeCalculator:
    _DAY_SECONDS = 86400
    _HOUR_SECONDS = 3600
    _MINUTE_SECONDS = 60

    def diff(self, start_time, end_time):
        start_dt = self._normalize_time(start_time)
        end_dt = self._normalize_time(end_time)
        delta = end_dt - start_dt
        total_seconds = abs(int(delta.total_seconds()))
        
        days = total_seconds // self._DAY_SECONDS
        remainder_after_days = total_seconds % self._DAY_SECONDS
        
        hours = remainder_after_days // self._HOUR_SECONDS
        remainder_after_hours = remainder_after_days % self._HOUR_SECONDS
        
        minutes = remainder_after_hours // self._MINUTE_SECONDS
        seconds = remainder_after_hours % self._MINUTE_SECONDS
        
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

    def _normalize_time(self, time_input):
        if isinstance(time_input, datetime.datetime):
            return time_input
        if isinstance(time_input, str):
            return datetime.datetime.fromisoformat(time_input)
        raise ValueError(f"Unsupported time type: {type(time_input)}")

if __name__ == '__main__':
    calculator = TimeCalculator()
    start = datetime.datetime(2023, 10, 1, 10, 0, 0)
    end = datetime.datetime(2023, 10, 5, 14, 30, 45)
    result = calculator.diff(start, end)
    print(result)
    
    start_str = "2023-10-01T10:00:00"
    end_str = "2023-10-01T12:05:10"
    result_str = calculator.diff(start_str, end_str)
    print(result_str)