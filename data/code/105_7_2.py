from datetime import date, timedelta

DAY_NAMES = {
    0: "Monday",
    1: "Tuesday",
    2: "Wednesday",
    3: "Thursday",
    4: "Friday",
    5: "Saturday",
    6: "Sunday",
}

TARGET_WEEKDAY = 1

REFERENCE_DATE = date(2023, 7, 4)

def calculate_next_weekday(start: date, target_weekday: int) -> date:
    current_weekday = start.weekday()
    days_until_target = (target_weekday - current_weekday + 7) % 7
    if days_until_target == 0:
        days_until_target = 7
    return start + timedelta(days=days_until_target)

if __name__ == '__main__':
    target_date = calculate_next_weekday(REFERENCE_DATE, TARGET_WEEKDAY)
    day_name = DAY_NAMES[target_date.weekday()]
    print(f"{day_name} ({target_date})")