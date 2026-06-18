from datetime import date
def calculate_past_date(years_to_subtract: int) -> str:
    current = date.today()
    return f"{current.year - years_to_subtract}-{current.month:02d}-{current.day:02d}"
if __name__ == '__main__':
    print(calculate_past_date(5))