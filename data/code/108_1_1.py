import datetime
def determine_day(date_string):
    date_object = datetime.datetime.strptime(date_string, '%Y-%m-%d')
    return date_object.day
if __name__ == '__main__':
    date1 = "2023-10-27"
    result1 = determine_day(date1)
    print(result1)
    date2 = "1999-01-01"
    result2 = determine_day(date2)
    print(result2)
    date3 = "2024-02-29"
    result3 = determine_day(date3)
    print(result3)