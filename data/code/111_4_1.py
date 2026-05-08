import datetime
def manipulate_date():
    start_date_str = "2023-10-26"
    days_to_add = 10
    start_date = datetime.datetime.strptime(start_date_str, "%Y-%m-%d").date()
    new_day = start_date.day + days_to_add
    if new_day > 31:
        new_month = start_date.month + (new_day - 31) // 30
        new_day = new_day % 30
        if new_month > 12:
            new_month = (new_month - 1) % 12 + 1
        if new_month == 12:
            new_year = start_date.year + (new_month - 1) // 12
        else:
            new_year = start_date.year
        if new_month == 1:
            new_year += 1
        result_date = datetime.date(new_year, new_month, new_day)
    else:
        try:
            result_date = datetime.date(start_date.year, start_date.month, new_day)
        except ValueError:
            result_date = datetime.date(start_date.year, start_date.month, new_day + 1)
    print(result_date.strftime("%Y-%m-%d"))
if __name__ == '__main__':
    manipulate_date()