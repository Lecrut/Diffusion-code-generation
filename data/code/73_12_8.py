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
        if days > 0:
            result = f"{days} days, {hours} hours"
        elif hours > 0:
            result = f"{hours} hours, {minutes} minutes"
        else:
            result = f"{minutes} minutes, {seconds} seconds"
        return result
if __name__ == '__main__':
    calculator = TimeCalculator()
    start1 = "2023-01-01T10:00:00"
    end1 = "2023-01-05T14:30:00"
    print(f"Difference between {start1} and {end1}: {calculator.diff(start1, end1)}")
    start2 = datetime(2023, 10, 20, 8, 0, 0)
    end2 = datetime(2023, 10, 22, 10, 15, 0)
    print(f"Difference between {start2} and {end2}: {calculator.diff(start2, end2)}")
    start3 = "2024-01-01T00:00:00"
    end3 = "2024-01-01T00:00:01"
    print(f"Difference between {start3} and {end3}: {calculator.diff(start3, end3)}")
    start4 = datetime(2024, 5, 1, 12, 0, 0)
    end4 = datetime(2024, 5, 1, 12, 5, 30)
    print(f"Difference between {start4} and {end4}: {calculator.diff(start4, end4)}")