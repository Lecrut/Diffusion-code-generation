import datetime
def calculate_future_date(start_date):
    if start_date is None:
        return None
    start_dt = datetime.datetime.strptime(start_date, "%Y-%m-%d").date()
    one_year_later = start_dt.replace(year=start_dt.year + 1)
    one_year_and_one_day_later = one_year_later + datetime.timedelta(days=1)
    return one_year_and_one_day_later.strftime("%Y-%m-%d")
if __name__ == '__main__':
    sample_date = "2023-10-26"
    result = calculate_future_date(sample_date)
    print(result)