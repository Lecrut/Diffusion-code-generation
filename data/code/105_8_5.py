import datetime
def calculate_future_date(start_date):
    if start_date is None:
        return None
    date_one_year_later = start_date.replace(year=start_date.year + 1)
    try:
        date_one_year_and_one_day_later = date_one_year_later + datetime.timedelta(days=1)
        return date_one_year_and_one_day_later
    except ValueError:
        return None
if __name__ == '__main__':
    sample_date_str = "2023-10-26"
    sample_date = datetime.datetime.strptime(sample_date_str, "%Y-%m-%d").date()
    result_date = calculate_future_date(sample_date)
    print(result_date.strftime("%Y-%m-%d"))