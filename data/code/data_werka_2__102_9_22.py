import datetime

def get_weekday_status(date_str):
    dt = datetime.datetime.strptime(date_str, "%Y-%m-%d")
    weekday_map = {
        0: "Weekday",
        1: "Weekday",
        2: "Weekday",
        3: "Weekday",
        4: "Weekday",
        5: "Weekend",
        6: "Weekend"
    }
    return weekday_map[dt.weekday()]

if __name__ == '__main__':
    sample_dates = {
        "2023-10-23": "Monday",
        "2023-10-28": "Saturday",
        "2023-10-29": "Sunday"
    }
    for date_str, expected in sample_dates.items():
        status = get_weekday_status(date_str)
        print(f"{date_str}: {status}")