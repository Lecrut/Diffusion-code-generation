from datetime import date

def get_day_name(date_obj):
    if not isinstance(date_obj, date):
        raise ValueError("Input must be an instance of date")
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    return days[date_obj.weekday()]

if __name__ == '__main__':
    date1 = date(2023, 10, 25)
    print(f"Date: {date1}, Day of the week: {get_day_name(date1)}")
    assert get_day_name(date1) == "Friday"

    date2 = date(2024, 1, 1)
    print(f"Date: {date2}, Day of the week: {get_day_name(date2)}")
    assert get_day_name(date2) == "Tuesday"

    try:
        get_day_name("2025-05-10")
    except ValueError as e:
        print(e)

    date3 = date(2025, 12, 31)
    print(f"Date: {date3}, Day of the week: {get_day_name(date3)}")
    assert get_day_name(date3) == "Saturday"