from datetime import datetime

def group_dates_by_month(dates):
    grouped = {}
    for date_str in dates:
        date_obj = datetime.strptime(date_str, '%Y-%m-%d')
        month_year = date_obj.strftime('%Y-%m')
        if month_year not in grouped:
            grouped[month_year] = []
        grouped[month_year].append(date_str)
    return grouped

if __name__ == '__main__':
    sample_dates = ['2023-01-15', '2023-02-20', '2023-01-25', '2024-03-10']
    result = group_dates_by_month(sample_dates)
    print(result)