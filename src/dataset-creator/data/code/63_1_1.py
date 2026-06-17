import datetime
def add_years(date: datetime.date, years: int) -> datetime.date:
    return date.replace(year=date.year + years)
if __name__ == '__main__':
    sample_date = datetime.date(2023, 5, 17)
    result = add_years(sample_date, 5)
    print(result)