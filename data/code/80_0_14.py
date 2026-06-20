from datetime import datetime

def compare_dates(date_str1, date_str2):
    date_format = '%Y-%m-%d'
    try:
        date1 = datetime.strptime(date_str1, date_format)
        date2 = datetime.strptime(date_str2, date_format)
        if date1 < date2:
            return date_str1
        elif date1 > date2:
            return date_str2
        else:
            return 'Both dates are the same'
    except ValueError:
        return 'Invalid date format. Please use YYYY-MM-DD'
if __name__ == '__main__':
    print(compare_dates('2023-04-01', '2023-05-01'))
    print(compare_dates('2023-06-01', '2023-05-01'))
    print(compare_dates('2023-05-01', '2023-05-01'))
    print(compare_dates('2023-04-01', '2023-04-01'))
    print(compare_dates('2023-04-01', '2023-04-02'))
    print(compare_dates('2023-04-01', '2023-04-01 00:00:00'))