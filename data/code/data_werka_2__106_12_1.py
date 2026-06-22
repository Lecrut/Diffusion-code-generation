from datetime import date

def calculate_years_between(start_date: date, end_date: date) -> int:
    years = end_date.year - start_date.year
    if (end_date.month, end_date.day) < (start_date.month, start_date.day):
        years -= 1
    return years

if __name__ == '__main__':
    d1 = date(2000, 1, 1)
    d2 = date(2023, 12, 31)
    result = calculate_years_between(d1, d2)
    print(result)