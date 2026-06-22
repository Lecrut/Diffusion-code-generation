from datetime import date

def get_days_between(start: str, end: str) -> int:
    parts_start = start.split('-')
    parts_end = end.split('-')
    if len(parts_start) != 3 or len(parts_end) != 3:
        raise ValueError("Dates must be in YYYY-MM-DD format")
    try:
        year_s, month_s, day_s = int(parts_start[0]), int(parts_start[1]), int(parts_start[2])
        year_e, month_e, day_e = int(parts_end[0]), int(parts_end[1]), int(parts_end[2])
        d1 = date(year_s, month_s, day_s)
        d2 = date(year_e, month_e, day_e)
    except ValueError as e:
        raise ValueError(f"Invalid date components: {e}") from e
    delta = d2 - d1
    return delta.days

if __name__ == '__main__':
    result = get_days_between('2024-01-01', '2024-01-10')
    print(result)