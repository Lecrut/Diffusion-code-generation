import datetime
def add_months(date_str: str, months_to_add: int) -> str:
    date_obj = datetime.datetime.strptime(date_str, "%Y-%m-%d")
    year, month = date_obj.year + (months_to_add // 12), date_obj.month + (months_to_add % 12)
    while month > 12:
        month -= 12
        year += 1
    while month < 1:
        month += 12
        year -= 1
    new_date = datetime.date(year, month, date_obj.day)
    return new_date.strftime("%Y-%m-%d")
if __name__ == '__main__':
    input_str = "2023-10-31"
    months = 5
    result = add_months(input_str, months)
    print(result)