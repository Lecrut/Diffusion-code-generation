import datetime
def check_weekend(date_str):
    date_obj = datetime.datetime.strptime(date_str, '%Y-%m-%d')
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
    date3 = "2023-10-23"
    print(check_weekend(date3))