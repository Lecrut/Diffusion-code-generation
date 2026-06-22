import datetime

class TimeCalculator:
    def diff(self, start_time, end_time):
        if isinstance(start_time, str):
            start_time = datetime.datetime.fromisoformat(start_time)
        if isinstance(end_time, str):
            end_time = datetime.datetime.fromisoformat(end_time)
        
        delta = end_time - start_time
        total_seconds = int(delta.total_seconds())
        
        if total_seconds < 0:
            return "Negative time difference"
        
        days = total_seconds // 86400
        remaining_seconds = total_seconds % 86400
        hours = remaining_seconds // 3600
        remaining_seconds = remaining_seconds % 3600
        minutes = remaining_seconds // 60
        seconds = remaining_seconds % 60
        
        parts = []
        if days > 0:
            parts.append(f"{days} day{'s' if days != 1 else ''}")
        if hours > 0:
            parts.append(f"{hours} hour{'s' if hours != 1 else ''}")
        if minutes > 0:
            parts.append(f"{minutes} minute{'s' if minutes != 1 else ''}")
        if seconds > 0 or not parts:
            parts.append(f"{seconds} second{'s' if seconds != 1 else ''}")
        
        return ", ".join(parts)

if __name__ == '__main__':
    calculator = TimeCalculator()
    start = datetime.datetime(2023, 1, 1, 10, 0, 0)
    end = datetime.datetime(2023, 1, 5, 14, 30, 45)
    result = calculator.diff(start, end)
    print(result)