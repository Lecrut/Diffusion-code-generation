from datetime import datetime

def sort_dates(date_strings):
    date_formats = ['%Y-%m-%d', '%m/%d/%Y', '%d.%m.%Y']
    normalized_dates = []
    
    for date_str in date_strings:
        for fmt in date_formats:
            try:
                normalized_date = datetime.strptime(date_str, fmt)
                normalized_dates.append((normalized_date, date_str))
                break
            except ValueError:
                continue
    
    sorted_dates = [date_str for _, date_str in sorted(normalized_dates)]
    
    return sorted_dates

if __name__ == '__main__':
    sample_dates = ['2021-03-15', '04/10/2020', '16.12.2019']
    print(sort_dates(sample_dates))