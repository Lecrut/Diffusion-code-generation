import datetime

def get_day_of_week(year, month, day):
    date_obj = datetime.date(year, month, day)
    weekday_number = date_obj.weekday()
    day_names = [
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday"
    ]
    return day_names[weekday_number]

if __name__ == '__main__':
    sample_year = 1999
    sample_month = 12
    sample_day = 31
    computed_day = get_day_of_week(sample_year, sample_month, sample_day)
    print(computed_day)