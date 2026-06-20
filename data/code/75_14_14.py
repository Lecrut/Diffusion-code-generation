from datetime import date

def months_and_years_difference(date1, date2):
    years_diff = date2.year - date1.year
    months_diff = date2.month - date1.month
    if date2.day < date1.day:
        months_diff -= 1
    total_months = years_diff * 12 + months_diff
    return years_diff, months_diff, total_months

if __name__ == '__main__':
    sample_date1 = date(2010, 5, 15)
    sample_date2 = date(2023, 8, 20)
    years_diff, months_diff, total_months = months_and_years_difference(sample_date1, sample_date2)
    print(f"Years difference: {years_diff}")
    print(f"Months difference: {months_diff}")
    print(f"Total months difference: {total_months}")