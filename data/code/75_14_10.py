from datetime import date

def calculate_date_difference(date1, date2):
    years_diff = date2.year - date1.year
    months_diff = date2.month - date1.month
    days_diff = date2.day - date1.day
    
    if days_diff < 0:
        months_diff -= 1
        days_diff += (date1.replace(day=28) + timedelta(days=4)).day - date1.day
    if months_diff < 0:
        years_diff -= 1
        months_diff += 12
    
    return years_diff, months_diff

if __name__ == '__main__':
    date1 = date(2020, 5, 15)
    date2 = date(2023, 8, 20)
    print(calculate_date_difference(date1, date2))