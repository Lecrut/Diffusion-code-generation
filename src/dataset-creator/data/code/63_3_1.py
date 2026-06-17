from datetime import datetime
def add_years(date_str: str, years: int) -> str:
    dt = datetime.strptime(date_str, "%Y-%m-%d")
    new_dt = dt.replace(year=dt.year + years)
    return new_dt.isoformat()
if __name__ == '__main__':
    sample_date = "2023-10-05"
    sample_years = 5
    result = add_years(sample_date, sample_years)
    print(result)