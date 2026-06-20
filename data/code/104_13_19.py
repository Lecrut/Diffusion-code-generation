from datetime import datetime

def same_week(date1: str, date2: str) -> bool:
    format_str = '%Y-%m-%d'
    dt1 = datetime.strptime(date1, format_str)
    dt2 = datetime.strptime(date2, format_str)
    return dt1.isocalendar()[1] == dt2.isocalendar()[1]
if __name__ == '__main__':
    print(same_week('2023-10-01', '2023-10-07'))
    print(same_week('2023-10-01', '2023-10-08'))