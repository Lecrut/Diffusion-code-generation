from datetime import datetime

def compare_dates(date_str1: str, date_str2: str) -> int:
    date_format = '%Y-%m-%d'
    parsed_date1 = datetime.strptime(date_str1, date_format)
    parsed_date2 = datetime.strptime(date_str2, date_format)
    if parsed_date1 < parsed_date2:
        return -1
    elif parsed_date1 > parsed_date2:
        return 1
    else:
        return 0
if __name__ == '__main__':
    sample_date_1 = '2023-05-01'
    sample_date_2 = '2023-06-01'
    result = compare_dates(sample_date_1, sample_date_2)
    print(result)