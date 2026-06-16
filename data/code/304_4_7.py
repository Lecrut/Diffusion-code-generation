import datetime
def check_precedence(date_a: str, date_b: str) -> bool:
    format_str = '%m/%d/%Y'
    try:
        date_a_obj = datetime.datetime.strptime(date_a, format_str)
        date_b_obj = datetime.datetime.strptime(date_b, format_str)
        return date_a_obj < date_b_obj
    except ValueError:
        return False
if __name__ == '__main__':
    print(check_precedence('01/15/2023', '03/20/2023'))
    print(check_precedence('12/31/2022', '01/01/2023'))
    print(check_precedence('05/05/2024', '05/05/2024'))
    print(check_precedence('06/01/2023', '06/01/2023'))
    print(check_precedence('10/10/2023', '10/10/2022'))