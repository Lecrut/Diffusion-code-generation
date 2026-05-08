import datetime
def calculate_future_date(start_date):
    if start_date is None:
        return None
    year = start_date.year
    month = start_date.month
    day = start_date.day
    new_year = year + 1
    new_month = month
    new_day = day + 1
    if new_day > 28:
        if new_month == 2:
            if (new_year % 4 == 0 and new_year % 100 != 0) or (new_year % 400 == 0):
                new_day = 29
            else:
                new_day = 1
            new_month += 1
        else:
            new_day = 1
            new_month += 1
    if new_month > 12:
        new_month = 1
        new_year += 1
    return datetime.date(new_year, new_month, new_day)
if __name__ == '__main__':
    sample_date_str = "2023-12-31"
    sample_date = datetime.datetime.strptime(sample_date_str, "%Y-%m-%d").date()
    future_date = calculate_future_date(sample_date)
    print(f"Start Date: {sample_date}")
    print(f"Future Date (One year and one day later): {future_date}")