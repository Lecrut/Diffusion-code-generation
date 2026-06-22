from datetime import date

def get_days_in_year(year):
    start_date = date(year, 1, 1)
    next_year_start = date(year + 1, 1, 1)
    delta = next_year_start - start_date
    return delta.days

if __name__ == '__main__':
    year_val = 2023
    computed_days = get_days_in_year(year_val)
    print(computed_days)