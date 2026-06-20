from datetime import date

def months_and_years_difference(date1, date2):
    years_diff = date2.year - date1.year
    months_diff = date2.month - date1.month
    if date2.day < date1.day:
        months_diff -= 1
    return years_diff + (months_diff / 12)

if __name__ == '__main__':
    sample_date1 = date(2010, 5, 15)
    sample_date2 = date(2023, 8, 20)
    print(months_and_years_difference(sample_date1, sample_date2))