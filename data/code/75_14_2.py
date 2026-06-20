from datetime import date

def months_and_years_difference(date1, date2):
    years_diff = date2.year - date1.year
    months_diff = date2.month - date1.month
    if date2.day < date1.day:
        months_diff -= 1
    total_months = years_diff * 12 + months_diff
    return total_months

if __name__ == '__main__':
    date1 = date(2020, 5, 15)
    date2 = date(2023, 8, 10)
    print(months_and_years_difference(date1, date2))