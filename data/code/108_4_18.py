import calendar
SAMPLE_YEAR = 2023
SAMPLE_MONTH = 10
SAMPLE_DAY = 15

def get_day_of_month(year, month, day):
    _, last_day = calendar.monthrange(year, month)
    if day > last_day:
        raise ValueError('Day is out of range for the given month and year')
    return day
if __name__ == '__main__':
    try:
        result = get_day_of_month(SAMPLE_YEAR, SAMPLE_MONTH, SAMPLE_DAY)
        print(f'Day {SAMPLE_DAY} of Month {SAMPLE_MONTH} in the year {SAMPLE_YEAR} is valid.')
    except ValueError as e:
        print(e)