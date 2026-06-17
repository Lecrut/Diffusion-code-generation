import datetime
def add_months(date_str: str, months_to_add: int) -> str:
    dt = datetime.datetime.strptime(date_str, "%Y-%m-%d")
    year = dt.year + (months_to_add // 12)
    month = dt.month - 1 + ((months_to_add % 12)) if months_to_add >= 0 else dt.month + abs(months_to_add % 12)
    while True:
        try:
            new_dt = datetime.datetime(year, int(month), dt.day)
            break
        except ValueError:
            month -= 1
    return new_dt.strftime("%Y-%m-%d")
if __name__ == '__main__':
    date_input = "2023-10-31"
    months_addition = -5
    result_date = add_months(date_input, months_addition)
    print(result_date)