from datetime import date
def calculate_past_date(years_to_subtract: int) -> str:
    today = date.today()
    past_year = today.year - years_to_subtract
    month = today.month
    day = today.day
    try:
        return f"{past_year}-{month:02d}-{day:02d}"
    except ValueError:
        if month == 12 and day > days_in_month(past_year, 1):
            return f"{past_year}-11-{days_in_month(past_year, 11)}"
        elif past_year < today.year:
            return f"{past_year}-{month:02d}-1"
def days_in_month(year: int, month: int) -> int:
    if month == 1 or month == 3 or month == 5 or month == 7 or\
       month == 8 or month == 10 or month == 12:
        return 31
    elif month in [4, 6, 9, 11]:
        return 30
    else:           
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            return 29
        return 28
if __name__ == '__main__':
    years = 5
    print(calculate_past_date(years))