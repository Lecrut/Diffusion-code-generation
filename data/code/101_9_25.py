import datetime

DAY_NAMES = {
    0: "MONDAY",
    1: "TUESDAY",
    2: "WEDNESDAY",
    3: "THURSDAY",
    4: "FRIDAY",
    5: "SATURDAY",
    6: "SUNDAY",
}

def get_day_of_week(date_string):
    parsed_date = datetime.datetime.strptime(date_string, "%Y-%m-%d")
    weekday_index = parsed_date.weekday()
    return DAY_NAMES[weekday_index]

if __name__ == '__main__':
    sample_date = "2023-11-11"
    day_name = get_day_of_week(sample_date)
    print(day_name)