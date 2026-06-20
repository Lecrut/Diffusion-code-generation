import datetime

def date_difference_seconds(date1: datetime.date, date2: datetime.date) -> tuple:
    if date1 > date2:
        date1, date2 = (date2, date1)
    delta = date2 - date1
    total_seconds = int(delta.total_seconds())
    hours = total_seconds // 3600
    minutes = total_seconds % 3600 // 60
    seconds = total_seconds % 60
    return (hours, minutes, seconds)
if __name__ == '__main__':
    d1 = datetime.date(2023, 1, 1)
    d2 = datetime.date(2023, 1, 10)
    result1 = date_difference_seconds(d1, d2)
    print(f'Hours: {result1[0]}, Minutes: {result1[1]}, Seconds: {result1[2]}')
    d3 = datetime.date(2024, 5, 15)
    d4 = datetime.date(2024, 4, 1)
    result2 = date_difference_seconds(d3, d4)
    print(f'Hours: {result2[0]}, Minutes: {result2[1]}, Seconds: {result2[2]}')