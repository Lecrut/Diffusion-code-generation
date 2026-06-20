import datetime
DAYS_OF_WEEK = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

def day_of_week(date_str):
    date_obj = datetime.datetime.strptime(date_str, '%Y-%m-%d')
    return DAYS_OF_WEEK[date_obj.weekday()]
if __name__ == '__main__':
    sample_date = '2023-10-05'
    print(day_of_week(sample_date))