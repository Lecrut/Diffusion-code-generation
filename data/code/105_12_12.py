import datetime

WEEKDAY_MAP = {
    "Monday": 0,
    "Tuesday": 1,
    "Wednesday": 2,
    "Thursday": 3,
    "Friday": 4,
    "Saturday": 5,
    "Sunday": 6
}

def get_next_weekday(start_date_str, target_weekday):
    start_date = datetime.datetime.strptime(start_date_str, "%Y-%m-%d").date()
    days_to_add = (WEEKDAY_MAP[target_weekday] - start_date.weekday()) % 7
    if days_to_add == 0:
        days_to_add = 7
    return (start_date + datetime.timedelta(days=days_to_add)).strftime("%Y-%m-%d")

if __name__ == '__main__':
    result = get_next_weekday("2023-10-01", "Friday")
    print(result)