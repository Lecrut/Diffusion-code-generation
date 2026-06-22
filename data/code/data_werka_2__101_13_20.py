import datetime

DAY_MAP = {
    0: "MONDAY",
    1: "TUESDAY",
    2: "WEDNESDAY",
    3: "THURSDAY",
    4: "FRIDAY",
    5: "SATURDAY",
    6: "SUNDAY",
}

def get_weekday(year, month, day):
    date_obj = datetime.date(year, month, day)
    index = date_obj.weekday()
    return DAY_MAP[index]

if __name__ == '__main__':
    result = get_weekday(2024, 7, 4)
    print(result)