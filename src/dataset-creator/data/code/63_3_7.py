from datetime import datetime, timedelta
def add_years(date_str: str, years: int) -> str:
    date_obj = datetime.strptime(date_str, "%Y-%m-%d")
    new_date = date_obj + timedelta(days=years * 365.2425)
    return new_date.strftime("%Y-%m-%d")
if __name__ == '__main__':
    sample_date = "2023-10-01"
    years_to_add = 5
    result = add_years(sample_date, years_to_add)
    print(result)