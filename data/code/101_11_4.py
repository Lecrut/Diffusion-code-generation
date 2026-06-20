from datetime import date

def get_day_of_week(year: int, month: int, day: int) -> str:
    weekday_names = {
        0: "Monday",
        1: "Tuesday",
        2: "Wednesday",
        3: "Thursday",
        4: "Friday",
        5: "Saturday",
        6: "Sunday"
    }
    date_obj = date(year, month, day)
    return weekday_names[date_obj.weekday()]

if __name__ == '__main__':
    print(get_day_of_week(2023, 10, 10))