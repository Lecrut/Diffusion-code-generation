def check_precedence(date_a: str, date_b: str) -> bool:
    try:
        month_a = int(date_a[:2])
        day_a = int(date_a[3:5])
        year_a = int(date_a[6:])
        month_b = int(date_b[:2])
        day_b = int(date_b[3:5])
        year_b = int(date_b[6:])
        date_a_tuple = (year_a, month_a, day_a)
        date_b_tuple = (year_b, month_b, day_b)
        return date_a_tuple < date_b_tuple
    except ValueError:
        return False
if __name__ == '__main__':
    print(check_precedence("01/15/2023", "02/01/2023"))
    print(check_precedence("12/31/2022", "01/01/2023"))
    print(check_precedence("05/10/2024", "05/10/2024"))
    print(check_precedence("06/01/2023", "06/01/2023"))
    print(check_precedence("10/20/2023", "11/15/2023"))
    print(check_precedence("01/01/2024", "12/31/2024"))
    print(check_precedence("03/01/2023", "03/01/2023"))