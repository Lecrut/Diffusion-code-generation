from datetime import date, timedelta
def calculate_past_date(years_to_subtract: int) -> str:
    today = date.today()
    past_date = today - timedelta(days=years_to_subtract * 365)
    return past_date.strftime("%Y-%m-%d")
if __name__ == '__main__':
    print(calculate_past_date(10))