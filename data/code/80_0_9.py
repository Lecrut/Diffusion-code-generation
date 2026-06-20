from datetime import datetime

def compare_dates(date1: str, date2: str) -> str:
    format_str = '%Y-%m-%d'
    datetime_obj1 = datetime.strptime(date1, format_str)
    datetime_obj2 = datetime.strptime(date2, format_str)
    if datetime_obj1 < datetime_obj2:
        return date1
    elif datetime_obj1 > datetime_obj2:
        return date2
    else:
        return 'Both dates are the same'
if __name__ == '__main__':
    earlier_date = compare_dates('2023-04-01', '2023-05-01')
    print(earlier_date)