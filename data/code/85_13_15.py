from datetime import datetime

def weeks_between_dates(date_str1: str, date_str2: str) -> int:
    date_format = '%Y-%m-%d'
    date1 = datetime.strptime(date_str1, date_format)
    date2 = datetime.strptime(date_str2, date_format)
    delta = abs((date2 - date1).days)
    return delta // 7

if __name__ == '__main__':
    sample_date1 = "2023-04-01"
    sample_date2 = "2023-05-15"
    print(weeks_between_dates(sample_date1, sample_date2))