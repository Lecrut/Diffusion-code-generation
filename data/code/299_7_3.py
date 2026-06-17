from datetime import datetime, time
def find_weekend_dates(date_strings):
    weekend_dates = []
    for date_str in date_strings:
        try:
            date_obj = datetime.strptime(date_str, "%Y-%m-%d").date()
            weekday = date_obj.weekday()
            if weekday >= 5:
                weekend_dates.append(date_str)
        except ValueError:
            continue
    return weekend_dates
if __name__ == '__main__':
    sample_dates = [
        "2023-10-27",
        "2023-10-28",
        "2023-10-29",
        "2023-10-30",
        "2023-10-31",
        "2023-11-01",
        "2023-11-02",
        "2023-11-03",
        "2023-11-04",
        "2023-11-05"
    ]
    result = find_weekend_dates(sample_dates)
    print(result)