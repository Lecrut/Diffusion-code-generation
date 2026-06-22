import datetime

WEEKDAY_NAMES = {
    0: "MONDAY",
    1: "TUESDAY",
    2: "WEDNESDAY",
    3: "THURSDAY",
    4: "FRIDAY",
    5: "SATURDAY",
    6: "SUNDAY",
}

def get_weekday_string(year, month, day):
    date_obj = datetime.date(year, month, day)
    weekday_index = date_obj.weekday()
    return WEEKDAY_NAMES[weekday_index]

if __name__ == '__main__':
    target_year = 2024
    target_month = 7
    target_day = 4
    result = get_weekday_string(target_year, target_month, target_day)
    print(result)