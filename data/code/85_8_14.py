import datetime
DAYS_IN_WEEK = 7

def date_difference_in_weeks(date1_str, date2_str):
    date1 = datetime.datetime.strptime(date1_str, '%Y-%m-%d')
    date2 = datetime.datetime.strptime(date2_str, '%Y-%m-%d')
    time_difference = abs((date1 - date2).days)
    difference_in_weeks = time_difference / DAYS_IN_WEEK
    return difference_in_weeks
if __name__ == '__main__':
    sample_date1 = '2023-01-01'
    sample_date2 = '2023-01-29'
    result = date_difference_in_weeks(sample_date1, sample_date2)
    print(result)