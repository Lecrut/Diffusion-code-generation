import datetime
ONE_YEAR_IN_DAYS = 365
ONE_MONTH_IN_DAYS = 30

def calculate_date_difference(date_str1, date_str2):
    date_format = '%Y-%m-%d'
    date1 = datetime.datetime.strptime(date_str1, date_format).date()
    date2 = datetime.datetime.strptime(date_str2, date_format).date()
    if date1 > date2:
        start_date = date2
        end_date = date1
    else:
        start_date = date1
        end_date = date2
    time_difference = end_date - start_date
    total_days = time_difference.days
    return total_days
if __name__ == '__main__':
    date_str1 = '2023-01-15'
    date_str2 = '2021-11-20'
    result = calculate_date_difference(date_str1, date_str2)
    print(f'Total days between {date_str1} and {date_str2}: {result}')