from datetime import datetime
DATE_FORMAT = '%Y-%m-%d'

def calculate_age_difference(date_str1, date_str2):
    date1 = datetime.strptime(date_str1, DATE_FORMAT)
    date2 = datetime.strptime(date_str2, DATE_FORMAT)
    age_diff = abs((date2 - date1).days) // 365
    return age_diff
if __name__ == '__main__':
    date1 = '1990-05-15'
    date2 = '2023-04-10'
    print(calculate_age_difference(date1, date2))