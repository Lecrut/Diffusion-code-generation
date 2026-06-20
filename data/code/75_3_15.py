from datetime import datetime

def date_difference(date_str1, date_str2):
    return abs(datetime.strptime(date_str1, '%Y-%m-%d') - datetime.strptime(date_str2, '%Y-%m-%d'))

if __name__ == '__main__':
    print(date_difference('2023-10-01', '2023-09-15'))