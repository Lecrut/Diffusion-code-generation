from datetime import date

def get_day_name(date_obj):
    days = {
        0: "Monday",
        1: "Tuesday",
        2: "Wednesday",
        3: "Thursday",
        4: "Friday",
        5: "Saturday",
        6: "Sunday"
    }
    return days[date_obj.weekday()]

if __name__ == '__main__':
    date1 = date(2023, 10, 25)
    print(f"Date: {date1}, Day of the week: {get_day_name(date1)}")
    assert get_day_name(date1) == "Sunday"

    date2 = date(2024, 1, 1)
    print(f"Date: {date2}, Day of the week: {get_day_name(date2)}")
    assert get_day_name(date2) == "Tuesday"

    date3 = date(2025, 12, 25)
    print(f"Date: {date3}, Day of the week: {get_day_name(date3)}")
    assert get_day_name(date3) == "Thursday"

    date4 = date(2026, 5, 10)
    print(f"Date: {date4}, Day of the week: {get_day_name(date4)}")
    assert get_day_name(date4) == "Saturday"