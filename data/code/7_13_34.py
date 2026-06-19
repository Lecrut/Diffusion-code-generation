from datetime import timedelta

def time_to_human_readable(time_str):
    hours, minutes, seconds = map(int, time_str.split(':'))
    total_seconds = hours * 3600 + minutes * 60 + seconds
    delta = timedelta(seconds=total_seconds)
    
    days = delta.days
    hours = delta.seconds // 3600
    minutes = (delta.seconds % 3600) // 60
    
    return f"{days} days, {hours} hours, {minutes} minutes"

if __name__ == '__main__':
    sample_time = '48:30:15'
    result = time_to_human_readable(sample_time)
    print(result)