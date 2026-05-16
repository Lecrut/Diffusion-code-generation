import datetime
class TimeScaler:
    def scale_time_differences(self, time_diff_strings):
        total_seconds = 0
        for ts in time_diff_strings:
            try:
                delta = datetime.timedelta(seconds=int(ts))
                total_seconds += delta.total_seconds()
            except ValueError:
                pass
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
        "86400",         
        "3600",           
        "1800",               
        "59"                  
    ]
    summary = scaler.scale_time_differences(sample_times)
    print(summary)