def check_precedence(date_a: str, date_b: str) -> bool:
    parts_a = date_a.split('/')
    parts_b = date_b.split('/')
    month_a = int(parts_a[0])
    day_a = int(parts_a[1])
    year_a = int(parts_a[2])
    month_b = int(parts_b[0])
    day_b = int(parts_b[1])
    year_b = int(parts_b[2])
    if year_a != year_b:
        return year_a < year_b
    elif month_a != month_b:
        return month_a < month_b
    else:
        return day_a < day_b
if __name__ == '__main__':
    print(check_precedence("01/15/2023", "02/01/2023"))
    print(check_precedence("12/31/2022", "01/01/2023"))
    print(check_precedence("05/10/2024", "05/10/2024"))
    print(check_precedence("10/20/2023", "10/21/2023"))
    print(check_precedence("03/01/2024", "03/01/2023"))