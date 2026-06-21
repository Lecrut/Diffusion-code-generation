from datetime import date

def calculate_full_year_difference(start_date: date, end_date: date) -> int:
    if start_date > end_date:
        start_date, end_date = end_date, start_date
    years = end_date.year - start_date.year
    if (end_date.month, end_date.day) < (start_date.month, start_date.day):
        years -= 1
    return years

if __name__ == '__main__':
    d1 = date(2023, 10, 15)
    d2 = date(2010, 5, 20)
    result = calculate_full_year_difference(d1, d2)
    print(result)