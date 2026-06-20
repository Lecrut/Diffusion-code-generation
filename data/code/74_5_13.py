from datetime import date

days_of_week = {
    0: "Monday",
    1: "Tuesday",
    2: "Wednesday",
    3: "Thursday",
    4: "Friday",
    5: "Saturday",
    6: "Sunday"
}

def get_day_name(date_obj):
    return days_of_week[date_obj.weekday()]

if __name__ == '__main__':
    date1 = date(2023, 10, 25)
    print(f"Date: {date1}, Day of the week: {get_day_name(date1)}")
    
    assert get_day_name(date1) == "Tuesday", f"Expected Tuesday, got {get_day_name(date1)}"
    
    date2 = date(2024, 1, 1)
    print(f"Date: {date2}, Day of the week: {get_day_name(date2)}")
    
    assert get_day_name(date2) == "Monday", f"Expected Monday, got {get_day_name(date2)}"
    
    date3 = date(2025, 12, 25)
    print(f"Date: {date3}, Day of the week: {get_day_name(date3)}")
    
    assert get_day_name(date3) == "Saturday", f"Expected Saturday, got {get_day_name(date3)}"
    
    date4 = date(2026, 5, 10)
    print(f"Date: {date4}, Day of the week: {get_day_name(date4)}")
    
    assert get_day_name(date4) == "Wednesday", f"Expected Wednesday, got {get_day_name(date4)}"