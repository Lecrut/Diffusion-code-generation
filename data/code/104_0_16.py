from datetime import datetime

def is_first_earlier(first: datetime, second: datetime) -> bool:
    first_year = first.year
    second_year = second.year
    if first_year != second_year:
        return first_year < second_year
    first_month = first.month
    second_month = second.month
    if first_month != second_month:
        return first_month < second_month
    first_day = first.day
    second_day = second.day
    if first_day != second_day:
        return first_day < second_day
    first_hour = first.hour
    second_hour = second.hour
    if first_hour != second_hour:
        return first_hour < second_hour
    first_minute = first.minute
    second_minute = second.minute
    if first_minute != second_minute:
        return first_minute < second_minute
    first_second = first.second
    second_second = second.second
    return first_second < second_second

if __name__ == '__main__':
    start_date = datetime(2024, 11, 5, 14, 30, 0)
    end_date = datetime(2024, 11, 5, 14, 30, 0)
    output = is_first_earlier(start_date, end_date)
    print(output)