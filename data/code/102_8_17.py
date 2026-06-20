from datetime import datetime

def is_weekday(iso_date_str):
    weekday_map = {
        0: False,
        1: True,
        2: True,
        3: True,
        4: True,
        5: False,
        6: False
    }
    date_obj = datetime.strptime(iso_date_str, "%Y-%m-%d")
    day_index = date_obj.weekday()
    return weekday_map[day_index]

if __name__ == '__main__':
    date1 = "2023-10-25"
    print(f"Date: {date1}, Is weekday: {is_weekday(date1)}")
    date2 = "2023-10-28"
    print(f"Date: {date2}, Is weekday: {is_weekday(date2)}")
    date3 = "2023-10-29"
    print(f"Date: {date3}, Is weekday: {is_weekday(date3)}")