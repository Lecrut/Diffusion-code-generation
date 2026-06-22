import datetime

def get_day_name(year, month, day):
    date_obj = datetime.date(year, month, day)
    weekdays = (
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday",
    )
    index = date_obj.weekday()
    return weekdays[index]

if __name__ == '__main__':
    sample_year = 2023
    sample_month = 10
    sample_day = 15
    result = get_day_name(sample_year, sample_month, sample_day)
    print(result)