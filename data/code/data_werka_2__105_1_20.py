import datetime

DAY_NAMES = {
    0: "Monday",
    1: "Tuesday",
    2: "Wednesday",
    3: "Thursday",
    4: "Friday",
    5: "Saturday",
    6: "Sunday"
}

def find_first_sunday_after_jan_1_2024():
    start_date = datetime.date(2024, 1, 1)
    target_weekday = 6
    days_to_add = (target_weekday - start_date.weekday()) % 7
    if days_to_add == 0:
        days_to_add = 7
    result_date = start_date + datetime.timedelta(days=days_to_add)
    return result_date

if __name__ == '__main__':
    computed_date = find_first_sunday_after_jan_1_2024()
    print(computed_date)