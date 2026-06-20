from datetime import datetime

class TimeCalculator:
    def diff(self, start_time, end_time):
        if isinstance(start_time, str):
            try:
                start_time = datetime.fromisoformat(start_time)
            except ValueError:
                raise ValueError("Invalid ISO 8601 format for start_time")
        
        if isinstance(end_time, str):
            try:
                end_time = datetime.fromisoformat(end_time)
            except ValueError:
                raise ValueError("Invalid ISO 8601 format for end_time")
        
        delta = abs(end_time - start_time)
        days = delta.days
        hours = delta.seconds // 3600
        
        return f'{days} days, {hours} hours'

if __name__ == '__main__':
    calculator = TimeCalculator()
    result = calculator.diff('2023-10-01T00:00:00', '2023-10-05T12:00:00')
    print(result)