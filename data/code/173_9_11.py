from datetime import datetime

def group_dates_by_month(dates):
    grouped = {}
    for date_str in dates:
        date_obj = datetime.strptime(date_str, '%Y-%m-%d')
        key = date_obj.strftime('%Y-%m')
        if key not in grouped:
            grouped[key] = []
        grouped[key].append(date_obj)
    return grouped

if __name__ == '__main__':
    sample_dates = ['2023-01-15', '2023-02-20', '2023-01-25', '2024-03-10']
    result = group_dates_by_month(sample_dates)
    print(result)