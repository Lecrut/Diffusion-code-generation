import datetime
class TimeScaler:
    def scale_time_differences(self, time_difference_strings):
        total_seconds = 0
        for time_str in time_difference_strings:
            try:
                if "days" in time_str.lower():
                    parts = time_str.split(" ")
                    if len(parts) == 2:
                        days = int(parts[0])
                        hours = int(parts[1])
                        total_seconds += (days * 24 * 3600) + (hours * 3600)
                elif "hours" in time_str.lower():
                    parts = time_str.split(" ")
                    if len(parts) == 2:
                        hours = int(parts[0])
                        total_seconds += hours * 3600
                elif "minutes" in time_str.lower():
                    parts = time_str.split(" ")
                    if len(parts) == 2:
                        minutes = int(parts[0])
                        total_seconds += minutes * 60
                elif "seconds" in time_str.lower():
                    parts = time_str.split(" ")
                    if len(parts) == 2:
                        seconds = int(parts[0])
                        total_seconds += seconds
                else:
                    pass
            except ValueError:
                continue
            except IndexError:
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
        "1 day 5 hours",
        "12 hours",
        "30 minutes",
        "100 seconds",
        "2 days 1 hour 30 minutes"
    ]
    result = scaler.scale_time_differences(sample_times)
    print(result)