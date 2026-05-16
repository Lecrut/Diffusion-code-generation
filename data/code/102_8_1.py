import datetime
def get_day_of_week_and_weekday(date_obj):
    day_names = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    day_index = date_obj.weekday()
    day_name = day_names[day_index]
    is_weekday = day_index < 6
    return day_name, is_weekday
if __name__ == '__main__':
    date1 = datetime.date(2023, 10, 25)
    date2 = datetime.date(2023, 10, 28)
    date3 = datetime.date(2023, 10, 29)
    date4 = datetime.date(2023, 10, 30)
    print(f"Date: {date1}, Day: {get_day_of_week_and_weekday(date1)[0]}, Weekday: {get_day_of_week_and_weekday(date1)[1]}")
    print(f"Date: {date2}, Day: {get_day_of_week_and_weekday(date2)[0]}, Weekday: {get_day_of_week_and_weekday(date2)[1]}")
    print(f"Date: {date3}, Day: {get_day_of_week_and_weekday(date3)[0]}, Weekday: {get_day_of_week_and_weekday(date3)[1]}")
    print(f"Date: {date4}, Day: {get_day_of_week_and_weekday(date4)[0]}, Weekday: {get_day_of_week_and_weekday(date4)[1]}")