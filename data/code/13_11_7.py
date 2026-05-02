import datetime
class TimeScaler:
    def scale_time_differences(self, time_difference_strings):
        total_seconds = 0
        for time_str in time_difference_strings:
            try:
                if 'days' in time_str.lower():
                    parts = time_str.split(' ')
                    if len(parts) >= 2:
                        days = int(parts[0])
                        hours = int(parts[1]) if len(parts) > 1 else 0
                        minutes = int(parts[2]) if len(parts) > 2 else 0
                        seconds = int(parts[3]) if len(parts) > 3 else 0
                        total_seconds += (days * 86400) + (hours * 3600) + (minutes * 60) + seconds
                elif 'hours' in time_str.lower():
                    parts = time_str.split(' ')
                    if len(parts) >= 2:
                        hours = int(parts[0])
                        minutes = int(parts[1]) if len(parts) > 1 else 0
                        seconds = int(parts[2]) if len(parts) > 2 else 0
                        total_seconds += (hours * 3600) + (minutes * 60) + seconds
                elif 'minutes' in time_str.lower():
                    parts = time_str.split(' ')
                    if len(parts) >= 2:
                        minutes = int(parts[0])
                        seconds = int(parts[1]) if len(parts) > 1 else 0
                        total_seconds += (minutes * 60) + seconds
                elif 'seconds' in time_str.lower():
                    try:
                        total_seconds += int(time_str)
                    except ValueError:
                        pass
            except Exception:
                continue
        total_seconds = int(total_seconds)
        days = total_seconds // 86400
        remaining_seconds = total_seconds % 86400
        hours = remaining_seconds // 3600
        remaining_seconds %= 3600
        minutes = remaining_seconds // 60
        seconds = remaining_seconds % 60
        return {
            "days": days,
            "hours": hours,
            "minutes": minutes,
            "seconds": seconds
        }
if __name__ == '__main__':
    scaler = TimeScaler()
    sample_times = [
        "1 day 5 hours 30 minutes 15 seconds",
        "2 days 0 hours 0 minutes 0 seconds",
        "10 hours 45 minutes 5 seconds",
        "300 minutes 10 seconds"
    ]
    result = scaler.scale_time_differences(sample_times)
    print(result)