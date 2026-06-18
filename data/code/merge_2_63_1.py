import datetime
def add_years(date: datetime.date, years: int) -> datetime.date:
    return date.replace(year=date.year + years)
if __name__ == '__main__':
    sample_date = datetime.date(2023, 10, 5)
    result_year = 5
    new_date = add_years(sample_date, result_year)
    print(new_date.strftime('%Y-%m-%d'))