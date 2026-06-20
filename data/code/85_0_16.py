import datetime

def calculate_week_difference(date_str1, date_str2):
    date_format = '%Y-%m-%d'
    date1 = datetime.datetime.strptime(date_str1, date_format)
    date2 = datetime.datetime.strptime(date_str2, date_format)
    time_difference = abs(date2 - date1)
    weeks = time_difference.days / 7.0
    return weeks

if __name__ == '__main__':
    sample_date1 = "2023-04-01"
    sample_date2 = "2023-05-08"
    result = calculate_week_difference(sample_date1, sample_date2)
    print(result)