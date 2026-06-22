import datetime

def determine_weekday(year, month, day):
    if month < 1 or month > 12:
        raise ValueError("Month must be between 1 and 12")
    if day < 1 or day > 31:
        raise ValueError("Day must be between 1 and 31")
    date_instance = datetime.date(year, month, day)
    return date_instance.strftime("%A")

if __name__ == '__main__':
    year_val = 2024
    month_val = 2
    day_val = 29
    computed_day = determine_weekday(year_val, month_val, day_val)
    print(computed_day)