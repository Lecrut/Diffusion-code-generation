from datetime import date

def calculate_months_difference(date1, date2):
    if not (isinstance(date1, date) and isinstance(date2, date)):
        raise ValueError("Both inputs must be instances of date.")
    
    months_diff = (date2.year - date1.year) * 12 + date2.month - date1.month
    return abs(months_diff)

if __name__ == '__main__':
    sample_date1 = date(2020, 5, 15)
    sample_date2 = date(2023, 8, 30)
    print(calculate_months_difference(sample_date1, sample_date2))