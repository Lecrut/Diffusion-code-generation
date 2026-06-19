class TimeScaler:
    def __init__(self):
        self.time_units = {'days': 0, 'hours': 0, 'minutes': 0, 'seconds': 0}

    def parse_time(self, time_str):
        parts = time_str.split()
        for part in parts:
            if 'day' in part:
                self.time_units['days'] += int(part.replace('day', '').replace('s', ''))
            elif 'hour' in part:
                self.time_units['hours'] += int(part.replace('hour', '').replace('s', ''))
            elif 'minute' in part:
                self.time_units['minutes'] += int(part.replace('minute', '').replace('s', ''))
            elif 'second' in part:
                self.time_units['seconds'] += int(part.replace('second', '').replace('s', ''))

    def summarize(self, time_list):
        for time_str in time_list:
            self.parse_time(time_str)
        return self.time_units

if __name__ == '__main__':
    sample_times = [
        "3 days 5 hours",
        "2 hours 45 minutes",
        "1 day 10 seconds",
        "60 minutes"
    ]
    scaler = TimeScaler()
    result = scaler.summarize(sample_times)
    print(result)