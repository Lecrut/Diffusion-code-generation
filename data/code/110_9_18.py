from datetime import datetime

def sort_date_strings(date_strings):
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
    
    sorted_dates = [date_str for _, date_str in sorted(normalized_dates)]
    
    return sorted_dates

if __name__ == '__main__':
    sample_dates = ['2023-10-05', '05/10/2023', '10-05-2023']
    print(sort_date_strings(sample_dates))