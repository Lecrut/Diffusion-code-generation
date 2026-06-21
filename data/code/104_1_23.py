def get_later_date(date1: str, date2: str) -> str:
    def validate_and_extract(date_str: str) -> tuple:
        if len(date_str) != 10 or date_str[4] != '-' or date_str[7] != '-':
            raise ValueError("Date must be in YYYY-MM-DD format")
        try:
            year = int(date_str[0:4])
            month = int(date_str[5:7])
            day = int(date_str[8:10])
        except ValueError:
            raise ValueError("Date components must be integers")
        if not (1 <= month <= 12):
            raise ValueError("Month must be between 1 and 12")
        if not (1 <= day <= 31):
            raise ValueError("Day must be between 1 and 31")
        return (year, month, day)

    y1, m1, d1 = validate_and_extract(date1)
    y2, m2, d2 = validate_and_extract(date2)

    if y1 > y2:
        return date1
    if y1 < y2:
        return date2
    if m1 > m2:
        return date1
    if m1 < m2:
        return date2
    if d1 > d2:
        return date1
    if d1 < d2:
        return date2
    return date1

if __name__ == '__main__':
    result = get_later_date("2023-10-15", "2023-10-16")
    print(result)