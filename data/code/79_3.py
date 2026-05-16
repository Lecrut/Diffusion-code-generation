from datetime import datetime
if __name__ == '__main__':
    today = datetime(2023, 10, 15)
    one_month_later = today.replace(month=today.month + 1, day=1)
    if one_month_later.month > 12:
        one_month_later = one_month_later.replace(year=one_month_later.year + 1, month=1)
    print(one_month_later)