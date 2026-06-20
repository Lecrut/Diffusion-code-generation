import datetime

def get_day_of_week(year, month, day):
    date = datetime.date(year, month, day)
    return date.strftime('%A')

if __name__ == '__main__':
    year_sample = 2024
    month_sample = 2
    day_sample = 29
    day_of_week = get_day_of_week(year_sample, month_sample, day_sample)
    print(f"The day of the week for February 29, 2024 is: {day_of_week}")