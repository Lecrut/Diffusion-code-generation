from datetime import datetime
DATE_FORMAT = '%Y-%m-%d'

def is_earlier(date1_str: str, date2_str: str) -> bool:
    try:
        date1 = datetime.strptime(date1_str, DATE_FORMAT)
        date2 = datetime.strptime(date2_str, DATE_FORMAT)
        return date1 < date2
    except ValueError:
        raise ValueError('One or both date strings are not in the expected YYYY-MM-DD format.')
if __name__ == '__main__':
    sample_date1 = '2023-10-26'
    sample_date2 = '2023-11-15'
    print(is_earlier(sample_date1, sample_date2))