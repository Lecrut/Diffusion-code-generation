from datetime import datetime

def calculate_days(date_str1, date_str2):
    try:
        date_format = '%Y-%m-%d'
        date1 = datetime.strptime(date_str1, date_format)
        date2 = datetime.strptime(date_str2, date_format)
        delta = abs((date2 - date1).days)
        return delta
    except (TypeError, ValueError) as e:
        print(f'Error: {e}')
        return None

if __name__ == '__main__':
    result = calculate_days('2023-01-01', '2023-01-31')
    print(result)