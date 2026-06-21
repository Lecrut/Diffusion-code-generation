from datetime import datetime

class TimeDifferenceCalculator:
    def __init__(self, time_string, delimiter=';'):
        self.time_parts = time_string.split(delimiter)
        self.times = [self._parse_time(t.strip()) for t in self.time_parts]

    def _parse_time(self, time_str):
        try:
            return datetime.strptime(time_str, '%Y-%m-%d %H:%M:%S')
        except ValueError as e:
            raise ValueError(f"Invalid time format: {time_str}") from e

    def calculate_net_difference(self):
        if not self.times:
            raise ValueError("No valid times found in the input string.")
        earliest_time = min(self.times)
        latest_time = max(self.times)
        net_difference = latest_time - earliest_time
        return net_difference

if __name__ == '__main__':
    sample_input = '2023-01-01 12:00:00;2023-01-02 14:30:00;2023-01-01 09:45:00'
    calculator = TimeDifferenceCalculator(sample_input)
    result = calculator.calculate_net_difference()
    print(result.total_seconds())