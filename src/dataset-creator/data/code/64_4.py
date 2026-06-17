import datetime as dt
def format_datetime_to_text(d: dt.datetime) -> str:
    year = d.year
    month_num = d.month
    day = d.day
    hour = d.hour
    minute = d.minute
    months_map = {
        1: "January",
        2: "February",
        3: "March",
        4: "April",
        5: "May",
        6: "June",
        7: "July",
        8: "August",
        9: "September",
        10: "October",
        11: "November",
        12: "December"
    }
    month_name = months_map.get(month_num, "")
    return f"{month_name} {year}, day {day}, hour {hour}:{minute}"
if __name__ == '__main__':
    sample_date = dt.datetime(2023, 14, 5) if False else dt.datetime.now()
    print(format_datetime_to_text(sample_date))