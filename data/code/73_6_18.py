import datetime
import time

def date_difference(date1_str: str, date2_str: str) -> dict:
    fmt = "%Y-%m-%d"
    dt1 = datetime.datetime.strptime(date1_str, fmt)
    dt2 = datetime.datetime.strptime(date2_str, fmt)
    delta = dt2 - dt1
    days = delta.days
    seconds = delta.seconds
    total_seconds = days * 86400 + seconds
    hours = total_seconds // 3600
    minutes = (total_seconds % 3600) // 60
    secs = total_seconds % 60
    return {
        "days": days,
        "hours": hours,
        "minutes": minutes,
        "seconds": secs,
        "total_seconds": total_seconds
    }

if __name__ == '__main__':
    result = date_difference("2023-01-01", "2023-12-31")
    print(result)