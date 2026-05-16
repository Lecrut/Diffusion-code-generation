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
    date2 = '2023-10-28'
    date3 = '2023-10-29'
    date4 = '2023-10-30'
    date5 = '2023-10-31'
    date6 = '2023-11-01'
    date7 = '2023-11-04'
    date8 = '2023-11-05'
    date9 = '2023-11-05'
    date10 = '2023-11-06'
    date11 = '2023-11-07'
    invalid_date = '2023/10/23'
    print(f"'{date1}': {check_weekday(date1)}")
    print(f"'{date2}': {check_weekday(date2)}")
    print(f"'{date3}': {check_weekday(date3)}")
    print(f"'{date4}': {check_weekday(date4)}")
    print(f"'{date5}': {check_weekday(date5)}")
    print(f"'{date6}': {check_weekday(date6)}")
    print(f"'{date7}': {check_weekday(date7)}")
    print(f"'{date8}': {check_weekday(date8)}")
    print(f"'{date9}': {check_weekday(date9)}")
    print(f"'{date10}': {check_weekday(date10)}")
    print(f"'{date11}': {check_weekday(date11)}")
    print(f"'{invalid_date}': {check_weekday(invalid_date)}")