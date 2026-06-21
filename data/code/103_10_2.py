from datetime import datetime, timedelta

def calculate_elapsed_time_since_start_of_day(target_date=None):
    if target_date is None:
        target_date = datetime(2023, 10, 5)
    
    start_of_day = target_date.replace(hour=0, minute=0, second=0, microsecond=0)
    elapsed = target_date - start_of_day
    
    total_seconds = int(elapsed.total_seconds())
    hours = total_seconds // 3600
    minutes = (total_seconds % 3600) // 60
    seconds = total_seconds % 60
    
    return {
        "target_date": target_date,
        "start_of_day": start_of_day,
        "elapsed_seconds": total_seconds,
        "elapsed_formatted": f"{hours}h {minutes}m {seconds}s"
    }

if __name__ == '__main__':
    sample_date = datetime(2023, 10, 5, 14, 30, 45)
    result = calculate_elapsed_time_since_start_of_day(sample_date)
    print(result["elapsed_formatted"])
    print(result["elapsed_seconds"])