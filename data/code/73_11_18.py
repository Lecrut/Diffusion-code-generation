import datetime

class TimeCalculator:
    def diff(self, start_time, end_time):
        try:
            if isinstance(start_time, str):
                start_time = datetime.datetime.fromisoformat(start_time)
            elif not isinstance(start_time, datetime.datetime):
                raise ValueError("start_time must be a datetime object or ISO 8601 string")
            
            if isinstance(end_time, str):
                end_time = datetime.datetime.fromisoformat(end_time)
            elif not isinstance(end_time, datetime.datetime):
                raise ValueError("end_time must be a datetime object or ISO 8601 string")
            
            delta = abs(end_time - start_time)
            days = delta.days
            hours = (delta.seconds // 3600) % 24
            return f'{days} days, {hours} hours'
        except ValueError as e:
            print(f"Error: {e}")
            return None

if __name__ == '__main__':
    calculator = TimeCalculator()
    result = calculator.diff('2023-10-01T00:00:00', '2023-10-05T12:00:00')
    print(result)