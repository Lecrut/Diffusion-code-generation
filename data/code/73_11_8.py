import datetime

TIME_UNITS = {
    'days': 86400,
    'hours': 3600,
    'minutes': 60,
}

class TimeCalculator:
    def diff(self, start_time, end_time):
        parsed_start = self._parse_time(start_time)
        parsed_end = self._parse_time(end_time)
        delta = abs(parsed_end - parsed_start)
        days, remainder = divmod(delta.total_seconds(), TIME_UNITS['days'])
        hours, remainder = divmod(remainder, TIME_UNITS['hours'])
        return f'{int(days)} days, {int(hours)} hours'

    def _parse_time(self, time_input):
        if isinstance(time_input, str):
            return datetime.datetime.fromisoformat(time_input)
        elif isinstance(time_input, datetime.datetime):
            return time_input
        else:
            raise ValueError("Unsupported time input type")

if __name__ == '__main__':
    calculator = TimeCalculator()
    result = calculator.diff('2023-10-01T00:00:00', '2023-10-05T12:00:00')
    print(result)