from datetime import datetime

days_of_week = {
    0: 'MONDAY',
    1: 'TUESDAY',
    2: 'WEDNESDAY',
    3: 'THURSDAY',
    4: 'FRIDAY',
    5: 'SATURDAY',
    6: 'SUNDAY'
}

def get_day_of_week(date_str):
    date_obj = datetime.strptime(date_str, '%Y-%m-%d')
    day_index = date_obj.weekday()
    return days_of_week[day_index]

if __name__ == '__main__':
    print(get_day_of_week('2023-11-11'))