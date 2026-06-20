from datetime import datetime

class TimeCalculator:
    def diff(self, start_time, end_time):
        if isinstance(start_time, str):
            start_time = datetime.fromisoformat(start_time)
        if isinstance(end_time, str):
            end_time = datetime.fromisoformat(end_time)
        
        delta = end_time - start_time
        days = delta.days
        hours = delta.seconds // 3600
        
        return f"{days} days, {hours} hours"

if __name__ == '__main__':
    calculator = TimeCalculator()
    result = calculator.diff("2023-10-01T00:00:00", "2023-10-05T14:30:00")
    print(result)