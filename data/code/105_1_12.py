from datetime import date, timedelta

DAY_NAMES = {
    0: "Monday",
    1: "Tuesday",
    2: "Wednesday",
    3: "Thursday",
    4: "Friday",
    5: "Saturday",
    6: "Sunday"
}

def find_first_sunday_after_reference():
    start_date = date(2024, 1, 1)
    days_in_week = 7
    target_weekday = 6
    current_weekday = start_date.weekday()
    days_to_add = (target_weekday - current_weekday) % days_in_week
    if days_to_add == 0:
        days_to_add = days_in_week
    target_date = start_date + timedelta(days=days_to_add)
    return target_date

if __name__ == '__main__':
    result = find_first_sunday_after_reference()
    print(result)