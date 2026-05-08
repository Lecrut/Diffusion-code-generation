import datetime
def check_weekday(date_string):
    try:
        date_obj = datetime.datetime.strptime(date_string, '%Y-%m-%d')
        weekday = date_obj.weekday()
        if 0 <= weekday <= 4:
            return 'Weekday'
        else:
            return 'Weekend'
    except ValueError:
        return 'Invalid Date Format'
if __name__ == '__main__':
    date1 = '2023-10-23'
    date2 = '2023-10-29'
    date3 = '2023-10-30'
    date4 = '2023-10-28'
    date5 = '2023-10-27'
    date_invalid = '2023/10/23'
    print(f"Date: {date1}, Result: {check_weekday(date1)}")
    print(f"Date: {date2}, Result: {check_weekday(date2)}")
    print(f"Date: {date3}, Result: {check_weekday(date3)}")
    print(f"Date: {date4}, Result: {check_weekday(date4)}")
    print(f"Date: {date5}, Result: {check_weekday(date5)}")
    print(f"Date: {date_invalid}, Result: {check_weekday(date_invalid)}")