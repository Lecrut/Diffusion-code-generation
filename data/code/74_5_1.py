from datetime import date
def get_day_name(date_obj):
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    day_index = date_obj.weekday()
    return days[day_index]
if __name__ == '__main__':
    date1 = date(2023, 10, 25)
    print(f"Date: {date1}, Day of the week: {get_day_name(date1)}")
    date2 = date(2024, 1, 1)
    print(f"Date: {date2}, Day of the week: {get_day_name(date2)}")
    date3 = date(2025, 12, 31)
    print(f"Date: {date3}, Day of the week: {get_day_name(date3)}")
    date4 = date(2023, 11, 10)
    print(f"Date: {date4}, Day of the week: {get_day_name(date4)}")