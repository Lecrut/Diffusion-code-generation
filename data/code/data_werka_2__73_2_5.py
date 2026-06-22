import datetime

class TimeCalculator:
    def calculate_difference(self, start_time, end_time):
        if not isinstance(start_time, datetime.datetime) or not isinstance(end_time, datetime.datetime):
            raise ValueError("Inputs must be datetime objects")
        delta = end_time - start_time
        total_seconds = delta.total_seconds()
        days = int(total_seconds // 86400)
        remaining_seconds = total_seconds % 86400
        hours = int(remaining_seconds // 3600)
        remaining_seconds = remaining_seconds % 3600
        minutes = int(remaining_seconds // 60)
        seconds = int(remaining_seconds % 60)
        return {
            "days": days,
            "hours": hours,
            "minutes": minutes,
            "seconds": seconds,
            "total_seconds": total_seconds
        }

if __name__ == '__main__':
    start = datetime.datetime(2023, 1, 1, 10, 0, 0)
    end = datetime.datetime(2023, 1, 5, 14, 30, 45)
    calculator = TimeCalculator()
    result = calculator.calculate_difference(start, end)
    print(result)