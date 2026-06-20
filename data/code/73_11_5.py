from datetime import datetime

class TimeCalculator:
    def diff(self, start_time, end_time):
        if isinstance(start_time, str):
            start_time = datetime.fromisoformat(start_time)
        if isinstance(end_time, str):
            end_time = datetime.fromisoformat(end_time)
        delta = abs(end_time - start_time)
        days = delta.days
        hours = delta.seconds // 3600
        return f'{days} days, {hours} hours'

if __name__ == '__main__':
    calculator = TimeCalculator()
    result1 = calculator.diff('2023-10-01T00:00:00', '2023-10-05T12:00:00')
    print(result1)
    result2 = calculator.diff(datetime(2023, 10, 1), datetime(2023, 10, 5, 12))
    print(result2)