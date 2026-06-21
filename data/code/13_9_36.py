from datetime import timedelta

class TimeScaler:

    def __init__(self):
        self.time_units = {'d': 86400, 'h': 3600, 'm': 60, 's': 1}

    def parse_time_differences(self, time_diff_list):
        total_seconds = 0
        for time_str in time_diff_list:
            if not time_str[-1] in self.time_units:
                raise ValueError(f'Unsupported time unit in {time_str}')
            value = int(time_str[:-1])
            unit = time_str[-1]
            total_seconds += value * self.time_units[unit]
        return self.seconds_to_summary(total_seconds)

    def seconds_to_summary(self, total_seconds):
        td = timedelta(seconds=total_seconds)
        days = td.days
        hours, remainder = divmod(td.seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        return {'days': days, 'hours': hours, 'minutes': minutes, 'seconds': seconds}
if __name__ == '__main__':
    time_scaler = TimeScaler()
    sample_times = ['5d', '3h', '45m', '10s']
    result = time_scaler.parse_time_differences(sample_times)
    print(result)