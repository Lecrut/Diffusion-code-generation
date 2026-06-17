import datetime
def check_weekend(date_string):
    date_obj = datetime.datetime.strptime(date_string, '%Y-%m-%d').date()
    weekday = date_obj.weekday()
    if weekday >= 5:
        return 'Weekend'
    else:
        return 'Weekday'
if __name__ == '__main__':
    date1 = "2023-10-21"
    print(check_weekend(date1))
    date2 = "2023-10-22"
    print(check_weekend(date2))
    date3 = "2023-10-28"
    print(check_weekend(date3))
    date4 = "2023-10-29"
    print(check_weekend(date4))