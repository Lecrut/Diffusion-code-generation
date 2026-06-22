def compare_dates(date1: str, date2: str) -> str:
    def parse_date(date_str: str) -> tuple:
        year = int(date_str[0:4])
        month = int(date_str[5:7])
        day = int(date_str[8:10])
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
    result = compare_dates("2023-10-01", "2023-09-15")
    print(result)