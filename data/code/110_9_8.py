from datetime import datetime

def sort_date_strings(date_strings):
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
    
    normalized_dates.sort()
    return [date_str for _, date_str in normalized_dates]

if __name__ == '__main__':
    sample_dates = ['2023-10-05', '10/06/2023', '07.11.2023']
    sorted_dates = sort_date_strings(sample_dates)
    print(sorted_dates)