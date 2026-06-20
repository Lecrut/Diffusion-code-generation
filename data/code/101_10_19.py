import calendar
SAMPLE_DATE = (2023, 12, 25)

def get_day_of_week(year, month, day):
    return calendar.day_name[calendar.weekday(year, month, day)]
if __name__ == '__main__':
    year, month, day = SAMPLE_DATE
    print(f'The day of the week for {month}/{year} is {get_day_of_week(year, month, day)}.')