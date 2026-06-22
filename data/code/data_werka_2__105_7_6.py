from datetime import date, timedelta

WEEKDAY_MAP: dict[int, str] = {
    0: "Monday",
    1: "Tuesday",
    2: "Wednesday",
    3: "Thursday",
    4: "Friday",
    5: "Saturday",
    6: "Sunday",
}

TARGET_WEEKDAY: int = 1
REFERENCE_DATE: date = date(2023, 7, 4)

def find_next_weekday(target: int, start: date) -> date:
    current_idx: int = start.weekday()
    days_offset: int = (target - current_idx) % 7
    if days_offset == 0:
        days_offset = 7
    return start + timedelta(days=days_offset)

def get_upcoming_tuesday() -> date:
    return find_next_weekday(TARGET_WEEKDAY, REFERENCE_DATE)

if __name__ == '__main__':
    result: date = get_upcoming_tuesday()
    print(result)