import calendar

def get_day_of_month(year, month, day):
    _, num_days = calendar.monthrange(year, month)
    return num_days

if __name__ == '__main__':
    year = 2023
    month = 10
    day = 15
    result = get_day_of_month(year, month, day)
    print(f"Day {day} of Month {month} in the year {year} falls on a day number: {result}")