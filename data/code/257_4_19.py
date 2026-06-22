from datetime import datetime
DATE_FORMAT = '%Y-%m-%d'

def calculate_date_difference(date_str1, date_str2):
    date_format = DATE_FORMAT
    date1 = datetime.strptime(date_str1, date_format)
    date2 = datetime.strptime(date_str2, date_format)
    return abs((date2 - date1).days)
if __name__ == '__main__':
    date_a = '2023-04-01'
    date_b = '2023-04-15'
    result = calculate_date_difference(date_a, date_b)
    print(result)