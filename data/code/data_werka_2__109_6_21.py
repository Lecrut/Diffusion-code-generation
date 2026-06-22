from datetime import datetime
import calendar

def _validate_dates(start: datetime, end: datetime) -> None:
    if not isinstance(start, datetime):
        raise ValueError("start must be a datetime object")
    if not isinstance(end, datetime):
        raise ValueError("end must be a datetime object")
    if start >= end:
        raise ValueError("start must be strictly before end")

def _get_days_in_month(year: int, month: int) -> int:
    if month < 1 or month > 12:
        raise ValueError("month must be between 1 and 12")
    return calendar.monthrange(year, month)[1]

def fraction_of_month_remaining(start: datetime, end: datetime) -> float:
    _validate_dates(start, end)
    
    if start.year != end.year or start.month != end.month:
        raise ValueError("start and end must be in the same month")
    
    days_in_month = _get_days_in_month(start.year, start.month)
    
    if days_in_month <= 0:
        raise ValueError("invalid days in month")
    
    start_day = start.day
    end_day = end.day
    
    if start_day == end_day:
        if start.hour == end.hour and start.minute == end.minute and start.second == end.second:
            return 0.0
        if start.time() >= end.time():
            return 0.0
    
    if start_day > end_day:
        return 0.0
    
    if start_day == end_day:
        remaining_seconds = (end - start).total_seconds()
        total_seconds = remaining_seconds
        if total_seconds <= 0:
            return 0.0
    else:
        remaining_days = end_day - start_day - 1
        remaining_seconds = remaining_days * 86400
        
        start_time_seconds = start.hour * 3600 + start.minute * 60 + start.second
        end_time_seconds = end.hour * 3600 + end.minute * 60 + end.second
        
        remaining_seconds += (86400 - start_time_seconds) + end_time_seconds
    
    now = datetime.now()
    
    if now < start:
        return 1.0
    
    if now > end:
        return 0.0
    
    elapsed_seconds = (now - start).total_seconds()
    
    if elapsed_seconds >= (end - start).total_seconds():
        return 0.0
    
    fraction_remaining = 1.0 - (elapsed_seconds / (end - start).total_seconds())
    
    if fraction_remaining < 0.0:
        fraction_remaining = 0.0
    if fraction_remaining > 1.0:
        fraction_remaining = 1.0
    
    return fraction_remaining

if __name__ == '__main__':
    start = datetime(2023, 1, 1, 0, 0, 0)
    end = datetime(2023, 1, 31, 23, 59, 59)
    result = fraction_of_month_remaining(start, end)
    print(f"Fraction remaining: {result}")