import re

class TimeScaler:
    def __init__(self):
        self.time_units = {'days': 0, 'hours': 0, 'minutes': 0, 'seconds': 0}

    def parse_time(self, time_str):
        match = re.match(r'(\d+)\s*(day|hour|minute|second)s?', time_str)
        if match:
            value, unit = int(match.group(1)), match.group(2) + 's'
            self.time_units[unit] += value

    def summarize(self, time_list):
        for time_str in time_list:
            self.parse_time(time_str)
        return self.time_units

if __name__ == '__main__':
    sample_times = [
        "5 days", "3 hours", "45 minutes", "10 seconds",
        "2 days", "1 hour", "59 minutes", "59 seconds"
    ]
    scaler = TimeScaler()
    result = scaler.summarize(sample_times)
    print(result)