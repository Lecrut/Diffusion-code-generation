import datetime

def calculate_week_difference(date_str1, date_str2):
    date_format = '%Y-%m-%d'
    date1 = datetime.datetime.strptime(date_str1, date_format)
    date2 = datetime.datetime.strptime(date_str2, date_format)
    time_difference = abs(date2 - date1)
    weeks = time_difference.days / 7.0
    return weeks

if __name__ == '__main__':
    dates = {
        'date1': "2023-01-01",
        'date2': "2023-01-08"
    }
    result = calculate_week_difference(dates['date1'], dates['date2'])
    print(result)