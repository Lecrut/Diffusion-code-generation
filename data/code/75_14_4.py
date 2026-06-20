from datetime import date

def months_and_years_difference(date1, date2):
    if not isinstance(date1, date) or not isinstance(date2, date):
        raise ValueError('Both inputs must be instances of date.')
    years_diff = date2.year - date1.year
    months_diff = date2.month - date1.month
    if date2.day < date1.day:
        months_diff -= 1
    total_months_diff = years_diff * 12 + months_diff
    return total_months_diff
if __name__ == '__main__':
    sample_date1 = date(2010, 5, 15)
    sample_date2 = date(2023, 8, 20)
    print(months_and_years_difference(sample_date1, sample_date2))