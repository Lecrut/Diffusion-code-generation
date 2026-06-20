from datetime import datetime

def months_between_dates(date1, date2):
    try:
        d1 = datetime.strptime(date1, '%Y-%m-%d')
        d2 = datetime.strptime(date2, '%Y-%m-%d')
        return (d2.year - d1.year) * 12 + (d2.month - d1.month)
    except ValueError as e:
        print(f'Invalid date format: {e}')
        return None
if __name__ == '__main__':
    result = months_between_dates('2020-01-01', '2023-04-15')
    print(result)