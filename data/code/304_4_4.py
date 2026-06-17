def check_precedence(date_a: str, date_b: str) -> bool:
    parts_a = list(map(int, date_a.split('/')))
    parts_b = list(map(int, date_b.split('/')))
    year_a, month_a, day_a = parts_a
    year_b, month_b, day_b = parts_b
    if year_a != year_b:
        return year_a < year_b
    elif month_a != month_b:
        return month_a < month_b
    else:
        return day_a < day_b
if __name__ == '__main__':
    print(check_precedence("01/15/2023", "02/20/2023"))
    print(check_precedence("12/31/2022", "01/01/2023"))
    print(check_precedence("05/10/2024", "05/10/2024"))
    print(check_precedence("10/01/2023", "10/01/2023"))
    print(check_precedence("06/01/2023", "06/02/2023"))
    print(check_precedence("11/30/2024", "12/01/2024"))
    print(check_precedence("03/01/2024", "03/01/2024"))