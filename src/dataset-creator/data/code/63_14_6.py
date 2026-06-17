import datetime
def get_future_dates(base_date: datetime.date, n_years: int) -> list[datetime.date]:
    return [base_date - datetime.timedelta(days=365 * i) for i in range(n_years)]
if __name__ == '__main__':
    sample_date = datetime.date(2024, 1, 15)
    result_dates = get_future_dates(sample_date, 5)
    print(result_dates)