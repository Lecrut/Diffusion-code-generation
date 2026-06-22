import datetime

DAY_NAMES = (
    "MONDAY",
    "TUESDAY",
    "WEDNESDAY",
    "THURSDAY",
    "FRIDAY",
    "SATURDAY",
    "SUNDAY",
)

def compute_weekday(year, month, day):
    date_instance = datetime.date(year, month, day)
    return DAY_NAMES[date_instance.weekday()]

if __name__ == '__main__':
    result = compute_weekday(2024, 7, 4)
    print(result)