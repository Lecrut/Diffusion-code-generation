import datetime
def check_weekend(date_str):
    date_obj = datetime.datetime.strptime(date_str, '%Y-%m-%d')
    weekday = date_obj.weekday()
    if weekday >= 5:
        return 'Weekend'
    else:
        return 'Weekday'
if __name__ == '__main__':
    date1 = '2023-10-28'
    print(check_weekend(date1))
    date2 = '2023-10-29'
    print(check_weekend(date2))
    date3 = '2023-10-30'
    print(check_weekend(date3))
    date4 = '2023-10-31'
    print(check_weekend(date4))