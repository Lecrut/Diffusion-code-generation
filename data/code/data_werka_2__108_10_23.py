import datetime

def get_day_name(year: int, month: int, day: int) -> str:
    date_obj = datetime.date(year, month, day)
    index = date_obj.weekday()
    mapping = {
        0: "Monday",
        1: "Tuesday",
        2: "Wednesday",
        3: "Thursday",
        4: "Friday",
        5: "Saturday",
        6: "Sunday",
    }
    return mapping[index]

if __name__ == '__main__':
    result = get_day_name(2024, 1, 1)
    print(result)