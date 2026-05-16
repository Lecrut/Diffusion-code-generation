import datetime
class TimeScaler:
    def scale_time_differences(self, time_difference_strings):
        total_seconds = 0
        for time_str in time_difference_strings:
            try:
                if "T" in time_str:
                    parts = time_str.split('T')
                    if len(parts) == 2:
                        time_part = parts[1]
                        if time_part:
                            time_components = time_part.split(':')
                            if len(time_components) == 3:
                                hours = int(time_components[0])
                                minutes = int(time_components[1])
                                seconds = int(time_components[2])
                                total_seconds += (hours * 3600) + (minutes * 60) + seconds
            except ValueError:
                continue
        total_seconds_in_day = total_seconds
        days = total_seconds_in_day // (24 * 3600)
        remaining_seconds = total_seconds_in_day % (24 * 3600)
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
        "2023-01-01T10:00:00",
        "2023-01-02T14:30:15",
        "2023-01-03T08:00:00"
    ]
    summary = scaler.scale_time_differences(sample_times)
    print(summary)