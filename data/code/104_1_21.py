def find_later_date(date_a: str, date_b: str) -> str:
    def to_days(date_str: str) -> int:
        year = int(date_str[0:4])
        month = int(date_str[5:7])
        day = int(date_str[8:10])
        y = year - 1
        m = month
        if m <= 2:
            y -= 1
            m += 12
        era = y // 400
        yoe = y - era * 400
        doy = (153 * (m - 3) + 2) // 5 + day - 1
        doe = yoe * 365 + yoe // 4 - yoe // 100 + doy
        return era * 146097 + doe - 719468
    if to_days(date_a) > to_days(date_b):
        return date_a
    if to_days(date_b) > to_days(date_a):
        return date_b
    return date_a

if __name__ == '__main__':
    print(find_later_date("2020-02-28", "2020-03-01"))