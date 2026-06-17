from datetime import date
def calculate_past_date(years_to_subtract: int) -> str:
    today = date.today()
    past_year = today.year - years_to_subtract
    return f"{past_year}-01-01"
if __name__ == '__main__':
    result = calculate_past_date(5)
    print(result)