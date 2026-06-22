from datetime import datetime

SECONDS_IN_MINUTE = 60
SECONDS_IN_HOUR = 3600
SECONDS_IN_DAY = 86400

def get_elapsed_time_since_midnight(reference_date):
    start_of_day = reference_date.replace(hour=0, minute=0, second=0, microsecond=0)
    delta = reference_date - start_of_day
    total_seconds = int(delta.total_seconds())
    
    days_part = total_seconds // SECONDS_IN_DAY
    remainder_after_days = total_seconds % SECONDS_IN_DAY
    
    hours_part = remainder_after_days // SECONDS_IN_HOUR
    remainder_after_hours = remainder_after_hours = remainder_after_days % SECONDS_IN_HOUR
    
    minutes_part = remainder_after_hours // SECONDS_IN_MINUTE
    seconds_part = remainder_after_hours % SECONDS_IN_MINUTE
    
    return {
        "reference": reference_date,
        "days": days_part,
        "hours": hours_part,
        "minutes": minutes_part,
        "seconds": seconds_part,
        "total_seconds": total_seconds
    }

if __name__ == '__main__':
    sample_date = datetime(2023, 10, 5, 14, 30, 45)
    result = get_elapsed_time_since_midnight(sample_date)
    print(result)