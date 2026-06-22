import datetime

DAY_MAPPING = {
    0: "MONDAY",
    1: "TUESDAY",
    2: "WEDNESDAY",
    3: "THURSDAY",
    4: "FRIDAY",
    5: "SATURDAY",
    6: "SUNDAY",
}

def get_day_of_week(date_string):
    date_obj = datetime.datetime.strptime(date_string, "%Y-%m-%d")
    return DAY_MAPPING[date_obj.weekday()]

if __name__ == '__main__':
    result = get_day_of_week("2023-11-11")
    print(result)