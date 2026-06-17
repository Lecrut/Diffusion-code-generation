import datetime
def get_future_dates(date_obj: datetime.date, n_years: int) -> list[datetime.date]:
    future_dates = []
    for i in range(1, n_years + 1):
        past_date = date_obj - datetime.timedelta(days=365 * i)
        try:
            adjusted_date = date_obj.replace(year=date_obj.year - (i))
            future_dates.append(adjusted_date)
        except ValueError:
            continue                                                                 
    return future_dates
if __name__ == '__main__':
    sample_date = datetime.date(2023, 10, 5)
    years_to_subtract = 4
    result = get_future_dates(sample_date, years_to_subtract)
    print(result)