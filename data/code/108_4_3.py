import calendar

def get_day_of_month(year, month, day):
    return calendar.monthrange(year, month)[1]

if __name__ == '__main__':
    year = 2023
    month = 4
    day = 15
    result = get_day_of_month(year, month, day)
    print(f"Day {day} of Month {month} in the year {year} falls on day number: {result}")