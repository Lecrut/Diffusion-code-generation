from datetime import datetime
from collections import defaultdict

def group_dates_by_month(dates):
    grouped = defaultdict(list)
    for date_str in dates:
        date_obj = datetime.strptime(date_str, '%Y-%m-%d')
        month_year = date_obj.strftime('%Y-%m')
        grouped[month_year].append(date_str)
    return dict(grouped)

if __name__ == '__main__':
    sample_dates = ['2023-01-15', '2023-02-20', '2023-01-25', '2024-03-05', '2024-03-10']
    result = group_dates_by_month(sample_dates)
    print(result)