from datetime import date

def compute_days_in_year(year):
    first_day = date(year, 1, 1)
    last_day = date(year, 12, 31)
    total_span = last_day - first_day
    return total_span.days

if __name__ == '__main__':
    target = 2023
    days = compute_days_in_year(target)
    print(days)