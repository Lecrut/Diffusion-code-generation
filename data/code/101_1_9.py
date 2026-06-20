import calendar

WEEKDAY_NAMES = [
    "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"
]

def get_weekday_name(year, month, day):
    date_obj = calendar.date(year, month, day)
    return WEEKDAY_NAMES[date_obj.weekday()]

if __name__ == '__main__':
    sample_year = 2023
    sample_month = 10
    sample_day = 26
    print(get_weekday_name(sample_year, sample_month, sample_day))