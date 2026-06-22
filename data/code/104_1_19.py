def compare_dates(date1: str, date2: str) -> str:
    def parse_date(d: str) -> tuple:
        parts = d.split('-')
        return (int(parts[0]), int(parts[1]), int(parts[2]))

    y1, m1, d1 = parse_date(date1)
    y2, m2, d2 = parse_date(date2)

    if y1 != y2:
        return date1 if y1 > y2 else date2
    if m1 != m2:
        return date1 if m1 > m2 else date2
    return date1 if d1 > d2 else date2

if __name__ == '__main__':
    result = compare_dates("2023-10-15", "2023-10-16")
    print(result)