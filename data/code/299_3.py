import datetime
def check_weekend(date_str):
    date_obj = datetime.datetime.strptime(date_str, '%Y-%m-%d').date()
    weekday = date_obj.weekday()
    if weekday >= 5:
        return 'Weekend'
    else:
        return 'Weekday'
if __name__ == '__main__':
    date1 = "2023-10-01"
    print(check_weekend(date1))
    date2 = "2023-10-08"
    print(check_weekend(date2))
    date3 = "2023-10-09"
    print(check_weekend(date3))