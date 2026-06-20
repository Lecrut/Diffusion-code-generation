from datetime import datetime

def dates_in_same_week(date_str1: str, date_str2: str) -> bool:
    date_format = '%Y-%m-%d'
    date1 = datetime.strptime(date_str1, date_format)
    date2 = datetime.strptime(date_str2, date_format)
    return date1.isocalendar()[1] == date2.isocalendar()[1]

if __name__ == '__main__':
    print(dates_in_same_week('2023-10-01', '2023-10-07'))
    print(dates_in_same_week('2023-10-01', '2023-10-08'))