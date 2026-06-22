from datetime import datetime, timedelta

def get_elapsed_time_since_day_start(reference_date):
    if not isinstance(reference_date, datetime):
        raise ValueError("reference_date must be a datetime object")
    
    start_of_day = reference_date.replace(hour=0, minute=0, second=0, microsecond=0)
    
    if start_of_day > reference_date:
        raise ValueError("reference_date must be on or after start_of_day")
        
    delta = reference_date - start_of_day
    total_seconds = int(delta.total_seconds())
    
    hours = total_seconds // 3600
    remainder = total_seconds % 3600
    minutes = remainder // 60
    seconds = remainder % 60
    
    return {
        "total_seconds": total_seconds,
        "formatted": f"{hours:02}:{minutes:02}:{seconds:02}"
    }

if __name__ == '__main__':
    sample_date = datetime(2023, 10, 5, 14, 30, 45)
    result = get_elapsed_time_since_day_start(sample_date)
    print(result['formatted'])