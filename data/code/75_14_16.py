from datetime import date

def calculate_date_difference(start_date, end_date):
    delta = end_date - start_date
    years_diff = delta.days // 365
    months_diff = (delta.days % 365) // 30
    return years_diff, months_diff

if __name__ == '__main__':
    start_date = date(2010, 1, 1)
    end_date = date(2023, 4, 1)
    print(calculate_date_difference(start_date, end_date))