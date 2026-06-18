from datetime import date, timedelta
def calculate_past_dates(years: int) -> list[date]:
    today = date.today()
    return [today - timedelta(days=365 * years)] if isinstance(years, int) else []
if __name__ == '__main__':
    sample_years = 10
    result = calculate_past_dates(sample_years)
    print(result[0])