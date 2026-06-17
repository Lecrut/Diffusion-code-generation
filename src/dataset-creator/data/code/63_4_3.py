from datetime import date
def calculate_past_date(years: int, month: int) -> str:
    today = date.today()
    past_year = today.year - years
    return f"{past_year}-{month:02d}-15"
if __name__ == '__main__':
    print(calculate_past_date(3, 7))