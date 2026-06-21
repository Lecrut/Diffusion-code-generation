from datetime import datetime

class TimeDifferenceCalculator:

    def __init__(self, time_string, delimiter=';'):
        self.time_parts = time_string.split(delimiter)
        self.times = [datetime.strptime(t.strip(), '%Y-%m-%d %H:%M:%S') for t in self.time_parts]

    def find_earliest_and_latest(self):
        return (min(self.times), max(self.times))

    def compute_net_difference(self, earliest_time, latest_time):
        return (latest_time - earliest_time).total_seconds()

    def calculate_net_time_difference(self):
        if not self.times:
            raise ValueError('No valid times found in the input string.')
        earliest_time, latest_time = self.find_earliest_and_latest()
        net_difference = self.compute_net_difference(earliest_time, latest_time)
        return net_difference
if __name__ == '__main__':
    sample_input = '2023-01-01 12:00:00;2023-01-05 18:45:00;2023-01-01 11:30:00'
    calculator = TimeDifferenceCalculator(sample_input)
    net_difference_seconds = calculator.calculate_net_time_difference()
    print(net_difference_seconds)