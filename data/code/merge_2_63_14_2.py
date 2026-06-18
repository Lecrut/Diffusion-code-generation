import datetime
def get_future_dates(base_date: datetime.date, n_years: int) -> list[datetime.date]:
    return [base_date.replace(year=base_date.year - i) for i in range(1, n_years + 1)]
if __name__ == '__main__':
    sample_base = datetime.date(2023, 5, 17)
    years_to_subtract = 4
    result_dates = get_future_dates(sample_base, years_to_subtract)
    print(result_dates)