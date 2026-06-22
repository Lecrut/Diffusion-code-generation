def compare_dates(date1: str, date2: str) -> str:
    def parse_date(date_str: str) -> tuple:
        parts = date_str.split('-')
        if len(parts) != 3:
            raise ValueError("Invalid date format")
        year, month, day = int(parts[0]), int(parts[1]), int(parts[2])
        if not (1 <= month <= 12):
            raise ValueError("Invalid month")
        if not (1 <= day <= 31):
            raise ValueError("Invalid day")
        return (year, month, day)

    d1 = parse_date(date1)
    d2 = parse_date(date2)

    if d1 > d2:
        return date1
    elif d2 > d1:
        return date2
    else:
        return date1

if __name__ == '__main__':
    result = compare_dates("2023-10-15", "2023-10-16")
    print(result)