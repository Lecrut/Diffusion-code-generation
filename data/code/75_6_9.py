import datetime

HOURS_PER_DAY = 24
MINUTES_PER_HOUR = 60
SECONDS_PER_MINUTE = 60

def date_difference(date1: datetime.date, date2: datetime.date) -> tuple:
    delta = abs(date2 - date1)
    total_seconds = int(delta.total_seconds())
    hours = total_seconds // (HOURS_PER_DAY * MINUTES_PER_HOUR * SECONDS_PER_MINUTE)
    minutes = (total_seconds % (HOURS_PER_DAY * MINUTES_PER_HOUR * SECONDS_PER_MINUTE)) // (MINUTES_PER_HOUR * SECONDS_PER_MINUTE)
    seconds = (total_seconds % (MINUTES_PER_HOUR * SECONDS_PER_MINUTE)) // SECONDS_PER_MINUTE
    return hours, minutes, seconds

if __name__ == '__main__':
    d1 = datetime.date(2023, 1, 1)
    d2 = datetime.date(2023, 1, 10)
    result1 = date_difference(d1, d2)
    print(f"Hours: {result1[0]}, Minutes: {result1[1]}, Seconds: {result1[2]}")
    
    d3 = datetime.date(2024, 5, 20)
    d4 = datetime.date(2024, 3, 15)
    result2 = date_difference(d3, d4)
    print(f"Hours: {result2[0]}, Minutes: {result2[1]}, Seconds: {result2[2]}")