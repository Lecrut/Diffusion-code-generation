import datetime

def days_left_in_month(date):
    year = date.year
    month = date.month
    if month == 12:
        next_month_start = datetime.date(year + 1, 1, 1)
    else:
        next_month_start = datetime.date(year, month + 1, 1)
    days_in_month = (next_month_start - datetime.date(year, month, 1)).days
    days_left = days_in_month - (date.day - 1)
    return days_left

def time_until_end_of_month(date):
    days_remaining = days_left_in_month(date)
    hours_remaining = 24 * days_remaining
    minutes_remaining = 60 * hours_remaining
    seconds_remaining = 60 * minutes_remaining
    return days_remaining, hours_remaining, minutes_remaining, seconds_remaining

if __name__ == '__main__':
    sample_date = datetime.date(2023, 10, 15)
    print(f"Days left until the end of the month: {days_left_in_month(sample_date)}")
    days, hours, minutes, seconds = time_until_end_of_month(sample_date)
    print(f"Time left until the end of the month: {days} days, {hours} hours, {minutes} minutes, {seconds} seconds")