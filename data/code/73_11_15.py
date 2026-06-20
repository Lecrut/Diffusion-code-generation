from datetime import datetime

class TimeCalculator:
    def diff(self, start_time, end_time):
        parsed_start = self.parse_time(start_time)
        parsed_end = self.parse_time(end_time)
        delta = abs(parsed_end - parsed_start)
        days = delta.days
        hours = delta.seconds // 3600
        return f'{days} days, {hours} hours'

    def parse_time(self, time_input):
        if isinstance(time_input, str):
            return datetime.fromisoformat(time_input)
        elif isinstance(time_input, datetime.datetime):
            return time_input
        else:
            raise ValueError("Unsupported time input type")

if __name__ == '__main__':
    calculator = TimeCalculator()
    result1 = calculator.diff('2023-10-01T00:00:00', '2023-10-05T12:00:00')
    print(result1)
    
    result2 = calculator.diff(datetime(2023, 10, 6, 14, 30), datetime(2023, 10, 7, 9, 0))
    print(result2)