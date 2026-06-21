from datetime import datetime

def group_dates_by_month(dates):
    GROUPED_DATES = {}
    DATE_FORMAT = '%Y-%m-%d'
    
    for date_str in dates:
        date_obj = datetime.strptime(date_str, DATE_FORMAT)
        month_year_key = date_obj.strftime('%Y-%m')
        
        if month_year_key not in GROUPED_DATES:
            GROUPED_DATES[month_year_key] = []
        
        GROUPED_DATES[month_year_key].append(date_str)
    
    return GROUPED_DATES

if __name__ == '__main__':
    sample_dates = ['2023-01-15', '2023-02-20', '2023-01-25', '2024-01-10']
    result = group_dates_by_month(sample_dates)
    print(result)