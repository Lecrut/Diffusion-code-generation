from datetime import datetime

def calculate_month_difference(date1, date2):
    try:
        d1 = datetime.strptime(date1, '%Y-%m-%d')
        d2 = datetime.strptime(date2, '%Y-%m-%d')
        return (d2.year - d1.year) * 12 + (d2.month - d1.month)
    except ValueError as e:
        print(f'Invalid date format: {e}')
        return None
if __name__ == '__main__':
    result = calculate_month_difference('2020-01-15', '2023-04-20')
    print(result)