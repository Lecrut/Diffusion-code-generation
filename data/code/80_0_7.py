from datetime import datetime

def earlier_date(date1: str, date2: str) -> str:
    format_str = '%Y-%m-%d'
    datetime_obj1 = datetime.strptime(date1, format_str)
    datetime_obj2 = datetime.strptime(date2, format_str)
    if datetime_obj1 < datetime_obj2:
        return date1
    else:
        return date2
if __name__ == '__main__':
    print(earlier_date('2023-01-01', '2023-01-02'))