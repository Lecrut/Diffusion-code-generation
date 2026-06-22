from datetime import datetime, timedelta

def calculate_time_difference(date1_str, date2_str):
    date_format = "%H:%M"
    time1 = datetime.strptime(date1_str, date_format)
    time2 = datetime.strptime(date2_str, date_format)
    
    if time2 < time1:
        time2 += timedelta(days=1)
    
    return (time2 - time1).total_seconds()

if __name__ == '__main__':
    sample_time1 = '23:59'
    sample_time2 = '00:01'
    diff_seconds = calculate_time_difference(sample_time1, sample_time2)
    print(f"Time difference in seconds: {diff_seconds}")