from datetime import datetime

def normalize_date(date_str):
    formats = ['%Y-%m-%d', '%d/%m/%Y', '%m-%d-%Y']
    for fmt in formats:
        try:
            return datetime.strptime(date_str, fmt)
        except ValueError:
            continue
    raise ValueError("Date format not recognized")

def sort_dates(date_strings):
    normalized_dates = [normalize_date(date) for date in date_strings]
    normalized_dates.sort()
    return [date.strftime('%Y-%m-%d') for date in normalized_dates]

if __name__ == '__main__':
    sample_dates = ['2021-03-15', '15/03/2021', '03-15-2021']
    print(sort_dates(sample_dates))