import datetime

DAY_NAMES = {
    0: "Monday",
    1: "Tuesday",
    2: "Wednesday",
    3: "Thursday",
    4: "Friday",
    5: "Saturday",
    6: "Sunday",
}

WEEKDAY_LIMIT = 5

def find_weekdays(date_strings):
    results = []
    for date_str in date_strings:
        parsed_date = datetime.datetime.strptime(date_str, "%Y-%m-%d")
        weekday_index = parsed_date.weekday()
        if weekday_index < WEEKDAY_LIMIT:
            day_name = DAY_NAMES[weekday_index]
            results.append((date_str, day_name))
    return results

if __name__ == '__main__':
    sample_dates = ["2023-10-01", "2023-10-02", "2023-10-07", "2023-10-08"]
    found = find_weekdays(sample_dates)
    print(found)