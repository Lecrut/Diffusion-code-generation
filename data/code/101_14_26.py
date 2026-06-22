import calendar
import datetime

MONTH_NAMES = {
    1: "January", 2: "February", 3: "March", 4: "April",
    5: "May", 6: "June", 7: "July", 8: "August",
    9: "September", 10: "October", 11: "November", 12: "December"
}

def determine_weekday(year: int, month: int, day: int) -> str:
    try:
        target_date = datetime.date(year, month, day)
    except ValueError as e:
        raise ValueError(f"Invalid date: {year}-{month}-{day}") from e
    
    weekday_index = target_date.weekday()
    weekday_name = calendar.day_name[weekday_index]
    month_name = MONTH_NAMES.get(month, "Unknown")
    
    return f"{weekday_name}, {month_name} {day}, {year}"

if __name__ == '__main__':
    result = determine_weekday(2025, 3, 15)
    print(result)