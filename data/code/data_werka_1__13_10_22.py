from datetime import timedelta

class TimeScaler:

    def __init__(self):
        self.time_units = {'d': 86400, 'h': 3600, 'm': 60, 's': 1}

    def parse_time_differences(self, time_diff_list):
        total_seconds = 0
        for time_str in time_diff_list:
            value, unit = (time_str[:-1], time_str[-1])
            if unit in self.time_units:
                total_seconds += int(value) * self.time_units[unit]
        return {'days': total_seconds // 86400, 'hours': total_seconds % 86400 // 3600, 'minutes': total_seconds % 3600 // 60, 'seconds': total_seconds % 60}
if __name__ == '__main__':
    sample_times = ['5d', '2h', '15m', '45s']
    scaler = TimeScaler()
    result = scaler.parse_time_differences(sample_times)
    print(result)