import datetime

JANUARY_FIRST_NAMES = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday"
]

def get_january_first_weekday(year):
    if year < 1:
        raise ValueError("Year must be a positive integer")
    target_date = datetime.date(year, 1, 1)
    day_index = target_date.weekday()
    return JANUARY_FIRST_NAMES[day_index]

if __name__ == '__main__':
    result = get_january_first_weekday(2024)
    print(result)