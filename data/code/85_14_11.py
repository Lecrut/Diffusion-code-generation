from datetime import timedelta

def weeks_difference(date1, date2):
    delta = abs((date2 - date1).days)
    return delta // 7
if __name__ == '__main__':
    sample_date1 = '2023-01-01'
    sample_date2 = '2023-01-15'
    date_format = '%Y-%m-%d'
    date1 = datetime.strptime(sample_date1, date_format)
    date2 = datetime.strptime(sample_date2, date_format)
    print(weeks_difference(date1, date2))