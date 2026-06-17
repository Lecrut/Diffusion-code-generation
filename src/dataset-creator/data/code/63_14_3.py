import datetime
def get_past_dates(base_date: datetime.date, years_subtracted: int) -> list[datetime.date]:
    return [base_date.replace(year=base_date.year - n) for n in range(1, years_subtracted + 1)]
if __name__ == '__main__':
    sample_date = datetime.date(2023, 5, 15)
    result_dates = get_past_dates(sample_date, 5)
    print(result_dates)