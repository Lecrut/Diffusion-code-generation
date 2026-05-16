import datetime
def get_day_of_week(date_string):
    date_obj = datetime.datetime.strptime(date_string, '%Y-%m-%d')
    day_of_week = date_obj.weekday()
    return day_of_week
if __name__ == '__main__':
    date_input = '2023-10-27'
    result = get_day_of_week(date_input)
    print(result)