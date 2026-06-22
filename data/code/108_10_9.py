import datetime

def get_day_of_week(year, month, day):
    date_obj = datetime.date(year, month, day)
    day_index = date_obj.weekday()
    day_names = {
        0: "Monday",
        1: "Tuesday",
        2: "Wednesday",
        3: "Thursday",
        4: "Friday",
        5: "Saturday",
        6: "Sunday"
    }
    return day_names[day_index]

if __name__ == '__main__':
    result = get_day_of_week(2024, 1, 1)
    print(result)