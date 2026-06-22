from datetime import date

YEAR_TO_MONTHS = {
    'year': 12,
    'month': 1,
    'day': 1 / 30.4375,
}

def calculate_year_difference(start_date: date, end_date: date) -> float:
    delta = end_date - start_date
    total_days = delta.days
    years_fraction = total_days * YEAR_TO_MONTHS['day']
    return years_fraction

if __name__ == '__main__':
    start = date(2010, 1, 1)
    end = date(2023, 6, 15)
    diff = calculate_year_difference(start, end)
    print(diff)