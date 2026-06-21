import datetime
import calendar

def determine_weekday(year, month, day):
    if not calendar.isleap(year) and month == 2 and day == 29:
        raise ValueError(f"Invalid date: {year}-{month:02d}-{day:02d}")
    date_instance = datetime.date(year, month, day)
    return date_instance.strftime("%A")

if __name__ == '__main__':
    target_year = 2024
    target_month = 2
    target_day = 29
    computed_day = determine_weekday(target_year, target_month, target_day)
    print(computed_day)