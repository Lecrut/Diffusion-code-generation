from datetime import datetime

def standardize_dates(date_list):
    standardized_dates = []
    date_formats = ['%m/%d/%Y', '%Y-%m-%d', '%A, %B %d, %Y']
    
    for date in date_list:
        for fmt in date_formats:
            try:
                parsed_date = datetime.strptime(date, fmt)
                standardized_date = parsed_date.strftime('%d/%m/%Y')
                standardized_dates.append(standardized_date)
                break
            except ValueError:
                continue
    
    return standardized_dates

if __name__ == '__main__':
    sample_dates = ['12/31/2020', '2021-01-01', 'Monday, January 04, 2021']
    print(standardize_dates(sample_dates))