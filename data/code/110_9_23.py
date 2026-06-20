from datetime import datetime

def normalize_date(date_str):
    date_formats = ['%Y-%m-%d', '%d/%m/%Y', '%m-%d-%Y']
    for fmt in date_formats:
        try:
            return datetime.strptime(date_str, fmt)
        except ValueError:
            continue
    raise ValueError(f"Invalid date format: {date_str}")

def sort_dates(date_strings):
    normalized_dates = [normalize_date(date_str) for date_str in date_strings]
    sorted_dates = sorted(normalized_dates)
    return [date.strftime('%Y-%m-%d') for date in sorted_dates]

if __name__ == '__main__':
    sample_dates = ['2021-03-15', '15/03/2021', '03-15-2021']
    print(sort_dates(sample_dates))