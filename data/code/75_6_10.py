import datetime

def date_difference_hours_minutes_seconds(date1: datetime.date, date2: datetime.date) -> tuple:
    if date1 > date2:
        delta = date1 - date2
    else:
        delta = date2 - date1
    
    total_seconds = int(delta.total_seconds())
    hours = total_seconds // 3600
    minutes = (total_seconds % 3600) // 60
    seconds = total_seconds % 60
    
    return hours, minutes, seconds

if __name__ == '__main__':
    d1 = datetime.date(2023, 4, 1)
    d2 = datetime.date(2023, 4, 5)
    result1 = date_difference_hours_minutes_seconds(d1, d2)
    print(f"Hours: {result1[0]}, Minutes: {result1[1]}, Seconds: {result1[2]}")
    
    d3 = datetime.date(2024, 7, 10)
    d4 = datetime.date(2024, 6, 15)
    result2 = date_difference_hours_minutes_seconds(d3, d4)
    print(f"Hours: {result2[0]}, Minutes: {result2[1]}, Seconds: {result2[2]}")