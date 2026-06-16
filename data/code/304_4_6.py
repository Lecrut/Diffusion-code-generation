def check_precedence(date_a: str, date_b: str) -> bool:
    format_str = '%m/%d/%Y'
    try:
        date_a_val = int(date_a.split('/')[0]), int(date_a.split('/')[1]), int(date_a.split('/')[2])
        date_b_val = int(date_b.split('/')[0]), int(date_b.split('/')[1]), int(date_b.split('/')[2])
        if date_a_val < date_b_val:
            return True
        else:
            return False
    except ValueError:
        return False
if __name__ == '__main__':
    print(check_precedence('01/15/2023', '02/20/2023'))
    print(check_precedence('12/31/2022', '01/01/2023'))
    print(check_precedence('05/05/2024', '05/05/2024'))
    print(check_precedence('10/10/2023', '10/10/2022'))