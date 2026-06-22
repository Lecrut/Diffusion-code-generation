from datetime import datetime

def check_weekends(dates):
    results = {}
    for date_str in dates:
        date_obj = datetime.strptime(date_str, '%Y-%m-%d')
        if date_obj.weekday() >= 5:
            results[date_str] = 'Weekend'
        else:
            results[date_str] = 'Not a Weekend'
    return results
if __name__ == '__main__':
    sample_dates = ['2023-10-07', '2023-10-08', '2023-10-09']
    print(check_weekends(sample_dates))