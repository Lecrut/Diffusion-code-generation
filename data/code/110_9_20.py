from datetime import datetime

def normalize_date(date_str):
    date_formats = ['%Y-%m-%d', '%d/%m/%Y', '%m-%d-%Y']
    for fmt in date_formats:
        try:
            return datetime.strptime(date_str, fmt)
        except ValueError:
            continue
    raise ValueError("Date format not recognized")

def sort_dates(date_strings):
    normalized_dates = [normalize_date(date) for date in date_strings]
    sorted_normalized_dates = sorted(normalized_dates)
    return [date.strftime('%Y-%m-%d') for date in sorted_normalized_dates]

if __name__ == '__main__':
    sample_dates = ['2023-01-25', '25/01/2023', '01-25-2023']
    print(sort_dates(sample_dates))