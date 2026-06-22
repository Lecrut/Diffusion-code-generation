import datetime

def calculate_time_left_in_month(start_date: datetime.datetime, end_date: datetime.datetime) -> dict:
    if start_date > end_date:
        raise ValueError("Start date must be before or equal to end date")
    if start_date == end_date:
        return {
            "days": 0,
            "hours": 0,
            "minutes": 0,
            "seconds": 0,
            "total_seconds": 0
        }
    days_remaining = (end_date - start_date).days
    hours_remaining = 24 - start_date.hour
    minutes_remaining = 60 - start_date.minute
    seconds_remaining = 60 - start_date.second

    if minutes_remaining == 60:
        minutes_remaining = 0
        hours_remaining -= 1
    if hours_remaining == 24:
        hours_remaining = 0
        days_remaining -= 1

    if seconds_remaining == 60:
        seconds_remaining = 0
        minutes_remaining -= 1
    if minutes_remaining == 60:
        minutes_remaining = 0
        hours_remaining -= 1

    total_seconds = (days_remaining * 86400) + (hours_remaining * 3600) + (minutes_remaining * 60) + seconds_remaining

    return {
        "days": days_remaining,
        "hours": hours_remaining,
        "minutes": minutes_remaining,
        "seconds": seconds_remaining,
        "total_seconds": total_seconds
    }

if __name__ == '__main__':
    start = datetime.datetime(2023, 10, 1, 10, 30, 45)
    end = datetime.datetime(2023, 10, 31, 23, 59, 59)
    result = calculate_time_left_in_month(start, end)
    print(result)