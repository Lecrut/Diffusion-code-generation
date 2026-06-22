import datetime

def compute_weekday_index(date_str: str) -> int:
    parts = date_str.split("-")
    if len(parts) != 3:
        raise ValueError("Invalid date format")
    year = int(parts[0])
    month = int(parts[1])
    day = int(parts[2])
    if not (1 <= month <= 12 and 1 <= day <= 31):
        raise ValueError("Invalid month or day")
    date_obj = datetime.date(year, month, day)
    return date_obj.weekday()

if __name__ == '__main__':
    target_date = '2024-07-04'
    weekday_index = compute_weekday_index(target_date)
    print(weekday_index)