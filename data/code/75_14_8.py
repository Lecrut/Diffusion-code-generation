from datetime import date

def calculate_date_difference(date1, date2):
    delta = abs(date2 - date1)
    years = delta.days // 365
    months = (delta.days % 365) // 30
    return years, months

if __name__ == '__main__':
    sample_date1 = date(2010, 5, 15)
    sample_date2 = date(2023, 8, 20)
    years, months = calculate_date_difference(sample_date1, sample_date2)
    print(f"Years: {years}, Months: {months}")