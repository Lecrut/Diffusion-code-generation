import datetime

def parse_time(time_input):
    if isinstance(time_input, str):
        return datetime.datetime.fromisoformat(time_input)
    elif isinstance(time_input, datetime.datetime):
        return time_input
    else:
        raise ValueError("Unsupported time input type")

class TimeCalculator:
    def diff(self, start_time, end_time):
        parsed_start = parse_time(start_time)
        parsed_end = parse_time(end_time)
        delta = abs(parsed_end - parsed_start)
        days = delta.days
        hours = delta.seconds // 3600
        return f'{days} days, {hours} hours'

if __name__ == '__main__':
    calculator = TimeCalculator()
    result = calculator.diff('2023-10-01T00:00:00', '2023-10-05T12:00:00')
    print(result)