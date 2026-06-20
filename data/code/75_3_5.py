from datetime import datetime

def date_difference(date_str1, date_str2):
    date_format = '%Y-%m-%d'
    date1 = datetime.strptime(date_str1, date_format)
    date2 = datetime.strptime(date_str2, date_format)
    return abs(date1 - date2)

if __name__ == '__main__':
    dates = {
        'date1': "2023-01-01",
        'date2': "2022-12-31"
    }
    difference = date_difference(dates['date1'], dates['date2'])
    print(difference)