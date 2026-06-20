from datetime import date

def months_and_years_difference(date1, date2):
    years_diff = abs(date2.year - date1.year)
    months_diff = abs(date2.month - date1.month)
    total_months_diff = (years_diff * 12) + months_diff
    
    if date2.day < date1.day:
        total_months_diff -= 1
    
    if date1 > date2:
        total_months_diff *= -1
    
    return total_months_diff

if __name__ == '__main__':
    sample_date1 = date(2015, 11, 1)
    sample_date2 = date(2023, 3, 31)
    print(months_and_years_difference(sample_date1, sample_date2))