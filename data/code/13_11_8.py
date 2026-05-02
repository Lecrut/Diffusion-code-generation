import re
from datetime import timedelta
class TimeScaler:
    def scale_time_differences(self, time_difference_strings: list[str]) -> dict:
        total_seconds = 0
        for time_str in time_difference_strings:
            match = re.match(r"(\d+)\s*h\s*,\s*(\d+)\s*m\s*,\s*(\d+)\s*s", time_str)
            if match:
                hours = int(match.group(1))
                minutes = int(match.group(2))
                seconds = int(match.group(3))
                total_seconds += (hours * 3600) + (minutes * 60) + seconds
            else:
                pass
        total_seconds_float = float(total_seconds)
        days = int(total_seconds_float // 86400)
        remaining_seconds = total_seconds_float % 86400
        hours = int(remaining_seconds // 3600)
        remaining_seconds %= 3600
        minutes = int(remaining_seconds // 60)
        seconds = int(remaining_seconds % 60)
        return {
            "days": days,
            "hours": hours,
            "minutes": minutes,
            "seconds": seconds
        }
if __name__ == '__main__':
    scaler = TimeScaler()
    sample_times = [
        "2\t1\t30\t0",
        "1\t12\t0\t0",
        "5\t0\t0\t0"
    ]
    result = scaler.scale_time_differences(sample_times)
    print(result)