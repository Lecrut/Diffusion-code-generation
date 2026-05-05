from datetime import datetime
class TimeCalculator:
    def diff(self, start_time, end_time):
        if isinstance(start_time, str):
            start = datetime.fromisoformat(start_time)
        elif isinstance(start_time, datetime):
            start = start_time
        else:
            raise TypeError("start_time must be a datetime object or an ISO 8601 string")
        if isinstance(end_time, str):
            end = datetime.fromisoformat(end_time)
        elif isinstance(end_time, datetime):
            end = end_time
        else:
            raise TypeError("end_time must be a datetime object or an ISO 8601 string")
        time_difference = end - start
        days = time_difference.days
        hours = time_difference.seconds
        minutes = time_difference.seconds % 60
        seconds = time_difference.seconds % 60
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
    start1 = "2023-01-01T10:00:00"
    end1 = "2023-01-05T14:30:15"
    print(f"Difference between '{start1}' and '{end1}': {calculator.diff(start1, end1)}")
    start2 = datetime(2023, 10, 20, 8, 0, 0)
    end2 = datetime(2023, 10, 22, 16, 45, 50)
    print(f"Difference between {start2} and {end2}: {calculator.diff(start2, end2)}")
    start3 = "2024-01-01T00:00:00"
    end3 = "2024-01-01T00:00:00"
    print(f"Difference between '{start3}' and '{end3}': {calculator.diff(start3, end3)}")
    start4 = "2023-12-31T23:59:59"
    end4 = "2024-01-01T00:00:01"
    print(f"Difference between '{start4}' and '{end4}': {calculator.diff(start4, end4)}")