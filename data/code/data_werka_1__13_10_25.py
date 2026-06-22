from datetime import timedelta

class TimeScaler:
    def __init__(self):
        self.time_units = {
            'd': 86400,
            'h': 3600,
            'm': 60,
            's': 1
        }

    def parse_time_differences(self, time_diff_strings):
        total_seconds = 0
        for time_str in time_diff_strings:
            if any(char.isdigit() for char in time_str):
                value, unit = '', ''
                for char in time_str:
                    if char.isdigit():
                        value += char
                    else:
                        unit += char
                if value and unit:
                    total_seconds += int(value) * self.time_units.get(unit[0], 0)
        
        return {
            'days': total_seconds // 86400,
            'hours': (total_seconds % 86400) // 3600,
            'minutes': (total_seconds % 3600) // 60,
            'seconds': total_seconds % 60
        }

if __name__ == '__main__':
    time_scaler = TimeScaler()
    sample_time_diffs = ['5d', '3h', '45m', '20s']
    result = time_scaler.parse_time_differences(sample_time_diffs)
    print(result)