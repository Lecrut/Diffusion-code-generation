from datetime import datetime

def sort_dates(date_strings):
    date_formats = ['%Y-%m-%d', '%d/%m/%Y', '%m-%d-%Y']
    normalized_dates = []
    
    for date_str in date_strings:
        for fmt in date_formats:
            try:
                normalized_date = datetime.strptime(date_str, fmt)
                normalized_dates.append(normalized_date)
                break
            except ValueError:
                continue
    
    return sorted(normalized_dates)

if __name__ == '__main__':
    sample_dates = ['2021-03-15', '15/03/2021', '03-15-2021']
    sorted_dates = sort_dates(sample_dates)
    print([date.strftime('%Y-%m-%d') for date in sorted_dates])