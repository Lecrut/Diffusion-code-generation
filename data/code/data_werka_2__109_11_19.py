import datetime
import calendar

def time_remaining_in_month(year, month):
    now = datetime.datetime.now()
    current_year = now.year
    current_month = now.month
    current_day = now.day
    current_hour = now.hour
    current_minute = now.minute
    current_second = now.second

    if year < current_year or (year == current_year and month < current_month):
        raise ValueError("The specified month and year are in the past.")

    days_in_month = calendar.monthrange(year, month)[1]
    
    if year == current_year and month == current_month:
        days_remaining = days_in_month - current_day
        hours_remaining = 24 - current_hour
        minutes_remaining = 60 - current_minute
        seconds_remaining = 60 - current_second
        
        if seconds_remaining == 60:
            seconds_remaining = 0
            minutes_remaining -= 1
        if minutes_remaining == 60:
            minutes_remaining = 0
            hours_remaining -= 1
        if hours_remaining == 24:
            hours_remaining = 0
            days_remaining -= 1
            
        total_seconds = (days_remaining * 24 * 3600) + (hours_remaining * 3600) + (minutes_remaining * 60) + seconds_remaining
    else:
        start_date = datetime.datetime(year, month, 1)
        end_date = datetime.datetime(year, month, days_in_month, 23, 59, 59)
        delta = end_date - now
        total_seconds = int(delta.total_seconds())
        
        if total_seconds < 0:
            raise ValueError("The specified month and year are in the past.")
            
        days_remaining = total_seconds // 86400
        remaining_seconds = total_seconds % 86400
        hours_remaining = remaining_seconds // 3600
        remaining_seconds %= 3600
        minutes_remaining = remaining_seconds // 60
        seconds_remaining = remaining_seconds % 60

    return days_remaining, hours_remaining, minutes_remaining, seconds_remaining

if __name__ == '__main__':
    days, hours, minutes, seconds = time_remaining_in_month(2024, 12)
    print(f"Days: {days}, Hours: {hours}, Minutes: {minutes}, Seconds: {seconds}")