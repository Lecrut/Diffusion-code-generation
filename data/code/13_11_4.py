import datetime
class TimeScaler:
    def scale_time_differences(self, time_difference_strings):
        total_seconds = 0
        for time_str in time_difference_strings:
            try:
                if "days" in time_str:
                    parts = time_str.split(" ")
                    days = int(parts[0])
                    total_seconds += days * 24 * 3600
                elif "hours" in time_str:
                    parts = time_str.split(" ")
                    hours = int(parts[0])
                    total_seconds += hours * 3600
                elif "minutes" in time_str:
                    parts = time_str.split(" ")
                    minutes = int(parts[0])
                    total_seconds += minutes * 60
                elif "seconds" in time_str:
                    parts = time_str.split(" ")
                    seconds = int(parts[0])
                    total_seconds += seconds
                else:
                    continue
            except (ValueError, IndexError):
                continue
        total_seconds = int(total_seconds)
        days = total_seconds // (24 * 3600)
        remaining_seconds = total_seconds % (24 * 3600)
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
        "2 days 10 hours 0 minutes 0 seconds",
        "30 minutes 45 seconds"
    ]
    summary = scaler.scale_time_differences(sample_times)
    print(summary)