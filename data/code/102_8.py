from datetime import date
def get_day_of_week_and_weekday(date_obj):
    day_names = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    day_index = date_obj.weekday()
    day_name = day_names[day_index]
    is_weekday = day_index < 5
    return day_name, is_weekday
if __name__ == '__main__':
    date1 = date(2023, 10, 25)
    day1, weekday1 = get_day_of_week_and_weekday(date1)
    print(f"Date: {date1}, Day of the week: {day1}, Is weekday: {weekday1}")
    date2 = date(2023, 10, 28)
    day2, weekday2 = get_day_of_week_and_weekday(date2)
    print(f"Date: {date2}, Day of the week: {day2}, Is weekday: {weekday2}")
    date3 = date(2023, 10, 29)
    day3, weekday3 = get_day_of_week_and_weekday(date3)
    print(f"Date: {date3}, Day of the week: {day3}, Is weekday: {weekday3}")