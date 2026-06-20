import calendar

def get_day_of_month(year, month, day):
    if not (1 <= year <= 9999) or not (1 <= month <= 12) or not (1 <= day <= 31):
        raise ValueError("Invalid date")
    
    try:
        return calendar.monthrange(year, month)[1]
    except ValueError as e:
        print(f"Error: {e}")
        return None

if __name__ == '__main__':
    year = 2023
    month = 4
    day = 15
    result = get_day_of_month(year, month, day)
    if result is not None:
        print(f"Day {day} of Month {month} in the year {year} falls on day number: {result}")