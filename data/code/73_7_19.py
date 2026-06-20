from datetime import datetime

def date_difference_in_minutes(date_str1, date_str2):
    format_str = '%Y-%m-%d %H:%M:%S'
    datetime_obj1 = datetime.strptime(date_str1, format_str)
    datetime_obj2 = datetime.strptime(date_str2, format_str)
    difference = abs((datetime_obj2 - datetime_obj1).total_seconds() / 60)
    return int(difference)

if __name__ == '__main__':
    result = date_difference_in_minutes('2023-10-01 12:00:00', '2023-10-01 14:30:00')
    print(result)