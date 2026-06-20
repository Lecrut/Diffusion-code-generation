from datetime import datetime

def days_between_dates(date_str1: str, date_str2: str) -> int:
    try:
        date_format = '%m/%d/%Y'
        date1 = datetime.strptime(date_str1, date_format)
        date2 = datetime.strptime(date_str2, date_format)
        return abs((date2 - date1).days)
    except ValueError as e:
        print(f'Invalid date format: {e}')
        return None
if __name__ == '__main__':
    result = days_between_dates('01/01/2023', '12/31/2022')
    print(result)