import datetime

def get_day_of_week(year, month, day):
    date = datetime.date(year, month, day)
    return date.strftime('%A')

if __name__ == '__main__':
    year = 2024
    month = 2
    day = 29
    print(f"The day of the week for {year}-{month:02d}-{day:02d} is {get_day_of_week(year, month, day)}")