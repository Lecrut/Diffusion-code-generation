import calendar

def get_day_of_month(year, month, day):
    _, last_day = calendar.monthrange(year, month)
    if day > last_day:
        raise ValueError("Day is greater than the last day of the month")
    return day

if __name__ == '__main__':
    YEAR = 2023
    MONTH = 10
    DAY = 15
    result = get_day_of_month(YEAR, MONTH, DAY)
    print(f"Day {DAY} of Month {MONTH} in the year {YEAR} falls on day number: {result}")