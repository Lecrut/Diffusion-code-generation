from datetime import datetime

def date_difference_in_minutes(date_str1, date_str2):
    date_format = '%Y-%m-%d %H:%M:%S'
    date1 = datetime.strptime(date_str1, date_format)
    date2 = datetime.strptime(date_str2, date_format)
    difference = abs((date2 - date1).total_seconds())
    return int(difference / 60)

if __name__ == '__main__':
    result = date_difference_in_minutes('2023-10-01 12:00:00', '2023-10-01 14:30:00')
    print(result)