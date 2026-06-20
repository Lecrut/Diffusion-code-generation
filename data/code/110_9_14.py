from datetime import datetime

def sort_dates(date_strings):
    date_formats = ['%Y-%m-%d', '%d/%m/%Y', '%m-%d-%Y']
    normalized_dates = []
    
    for date_str in date_strings:
        for fmt in date_formats:
            try:
                normalized_date = datetime.strptime(date_str, fmt)
                normalized_dates.append((normalized_date, date_str))
                break
            except ValueError:
                continue
    
    sorted_dates = [date[1] for date in sorted(normalized_dates)]
    
    return sorted_dates

if __name__ == '__main__':
    sample_dates = ['2023-01-01', '01/02/2023', '03-04-2022']
    print(sort_dates(sample_dates))