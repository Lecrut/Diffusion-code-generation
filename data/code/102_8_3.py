from datetime import date
def get_day_of_week(date_obj):
    day_names = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    day_index = date_obj.weekday()
    return day_names[day_index]
if __name__ == '__main__':
    date1 = date(2023, 10, 23)
    print(f"Date {date1}: {get_day_of_week(date1)}")
    date2 = date(2023, 10, 29)
    print(f"Date {date2}: {get_day_of_week(date2)}")
    date3 = date(2023, 10, 30)
    print(f"Date {date3}: {get_day_of_week(date3)}")
    date4 = date(2023, 10, 28)
    print(f"Date {date4}: {get_day_of_week(date4)}")