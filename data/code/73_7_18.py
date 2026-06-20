from datetime import datetime

def date_difference_in_minutes(date_str1, date_str2):
    date_format = '%Y-%m-%d %H:%M:%S'
    date1 = datetime.strptime(date_str1, date_format)
    date2 = datetime.strptime(date_str2, date_format)
    delta = abs(date2 - date1)
    return int(delta.total_seconds() / 60)

if __name__ == '__main__':
    result = date_difference_in_minutes('2023-10-05 14:30:00', '2023-10-05 15:45:00')
    print(result)