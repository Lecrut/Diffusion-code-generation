import datetime

SECONDS_PER_MINUTE = 60
MINUTES_PER_HOUR = 60
HOURS_PER_DAY = 24

def calculate_duration(date1, date2):
    time_difference = abs(date2 - date1)
    days = time_difference.days
    seconds = time_difference.seconds
    hours = seconds // SECONDS_PER_MINUTE // MINUTES_PER_HOUR
    minutes = (seconds // SECONDS_PER_MINUTE) % MINUTES_PER_HOUR
    return days, hours, minutes

if __name__ == '__main__':
    date1 = datetime.datetime(2023, 4, 1, 12, 0, 0)
    date2 = datetime.datetime(2023, 4, 1, 10, 30, 0)
    days, hours, minutes = calculate_duration(date1, date2)
    print(f"Duration: {days} day{'s' if days != 1 else ''}, {hours} hour{'s' if hours != 1 else ''}, {minutes} minute{'s' if minutes != 1 else ''}")