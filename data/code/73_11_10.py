import datetime

class TimeCalculator:
    def diff(self, start_time, end_time):
        start = self.parse_time(start_time)
        end = self.parse_time(end_time)
        if start > end:
            start, end = end, start
        delta = end - start
        days = delta.days
        hours = (delta.seconds // 3600) % 24
        return f'{days} days, {hours} hours'

    def parse_time(self, time_input):
        if isinstance(time_input, str):
            return datetime.datetime.fromisoformat(time_input)
        elif isinstance(time_input, datetime.datetime):
            return time_input
        else:
            raise ValueError("Unsupported time input type")

if __name__ == '__main__':
    calculator = TimeCalculator()
    result = calculator.diff('2023-10-05T12:00:00', '2023-10-01T00:00:00')
    print(result)