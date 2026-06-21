class TimeAggregator:
    def __init__(self):
        self.total_seconds = 0

    def add_time_difference(self, time_diff):
        parts = time_diff.split()
        if len(parts) != 2:
            raise ValueError(f"Invalid time difference format: {time_diff}")
        value, unit = parts
        try:
            value = int(value)
        except ValueError:
            raise ValueError(f"Invalid numeric value in time difference: {value}")
        if unit == 'hours':
            self.total_seconds += value * 3600
        elif unit == 'minutes':
            self.total_seconds += value * 60
        else:
            raise ValueError(f"Unsupported unit in time difference: {unit}")

    def get_total_seconds(self):
        return self.total_seconds

if __name__ == '__main__':
    sample_time_diffs = [
        "2 hours and 30 minutes",
        "1 hour 45 minutes",
        "30 minutes"
    ]

    aggregator = TimeAggregator()
    for diff in sample_time_diffs:
        try:
            aggregator.add_time_difference(diff)
        except ValueError as e:
            print(e)

    print(aggregator.get_total_seconds())