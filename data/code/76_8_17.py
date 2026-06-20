from datetime import datetime

def calculate_days(date_str1, date_str2):
    try:
        date_format = '%Y-%m-%d'
        date1 = datetime.strptime(date_str1, date_format)
        date2 = datetime.strptime(date_str2, date_format)
        delta = abs((date2 - date1).days)
        return delta
    except TypeError as e:
        print(f'TypeError: {e}')
        return None

if __name__ == '__main__':
    sample_dates = {
        'start_date': '2023-01-01',
        'end_date': '2023-01-31'
    }
    result = calculate_days(sample_dates['start_date'], sample_dates['end_date'])
    print(result)