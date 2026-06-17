import datetime
def generate_past_dates(base_date: datetime.date, n_years: int) -> list[datetime.date]:
    return [base_date.replace(year=base_date.year - i) for i in range(1, n_years + 1)]
if __name__ == '__main__':
    sample_date = datetime.date(2023, 5, 15)
    years_to_subtract = 4
    result_dates = generate_past_dates(sample_date, years_to_subtract)
    print(result_dates)