import calendar

def validate_date(year, month, day):
    if not (1 <= month <= 12) or not (1 <= day <= calendar.monthrange(year, month)[1]):
        raise ValueError("Invalid date")

def get_day_of_week(year, month, day):
    validate_date(year, month, day)
    return calendar.day_name[calendar.weekday(year, month, day)]

if __name__ == '__main__':
    sample_date = (2023, 12, 25)
    try:
        print(f"The day of the week for {sample_date[1]}/{sample_date[0]} is {get_day_of_week(*sample_date)}.")
    except ValueError as e:
        print(e)