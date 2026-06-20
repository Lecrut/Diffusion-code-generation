import datetime
TARGET_DATE = '2023-11-11'

def determine_day_of_week(date_str):
    date_obj = datetime.datetime.strptime(date_str, '%Y-%m-%d')
    day_index = date_obj.weekday()
    days_of_week = ['MONDAY', 'TUESDAY', 'WEDNESDAY', 'THURSDAY', 'FRIDAY', 'SATURDAY', 'SUNDAY']
    return days_of_week[day_index]
if __name__ == '__main__':
    result = determine_day_of_week(TARGET_DATE)
    print(result)