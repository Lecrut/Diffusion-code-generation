from datetime import datetime

def date_difference(date_str1, date_str2):
    date_format = '%Y-%m-%d'
    date1 = datetime.strptime(date_str1, date_format)
    date2 = datetime.strptime(date_str2, date_format)
    difference = abs((date2 - date1).days)
    return difference

if __name__ == '__main__':
    sample_date1 = '2023-05-01'
    sample_date2 = '2023-05-10'
    result = date_difference(sample_date1, sample_date2)
    print(result)