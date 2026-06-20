import datetime

if __name__ == '__main__':
    weekday_index = datetime.datetime.strptime('2023-12-25', '%Y-%m-%d').weekday()
    day_name = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'][weekday_index]
    print(day_name)