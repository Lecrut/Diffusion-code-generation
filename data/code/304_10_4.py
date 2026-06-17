from datetime import datetime
def is_date_before(date_str1, date_str2):
    date1 = datetime.strptime(date_str1, '%Y-%m-%d')
    date2 = datetime.strptime(date_str2, '%Y-%m-%d')
    return date1 < date2
if __name__ == '__main__':
    print(is_date_before('2023-01-15', '2023-01-16'))
    print(is_date_before('2023-01-16', '2023-01-15'))
    print(is_date_before('2023-01-15', '2023-01-15'))
    print(is_date_before('2024-05-20', '2024-05-21'))
    print(is_date_before('2024-12-31', '2024-01-01'))