import datetime

def get_january_first_weekday(year):
    target_date = datetime.date(year, 1, 1)
    weekday_index = target_date.weekday()
    weekday_mapping = [
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday"
    ]
    return weekday_mapping[weekday_index]

if __name__ == '__main__':
    sample_year = 2024
    computed_day = get_january_first_weekday(sample_year)
    print(computed_day)