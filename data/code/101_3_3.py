import datetime

if __name__ == '__main__':
    weekday_mapping = {0: 'Monday', 1: 'Tuesday', 2: 'Wednesday', 3: 'Thursday', 4: 'Friday', 5: 'Saturday', 6: 'Sunday'}
    date_obj = datetime.datetime.strptime('2023-12-25', '%Y-%m-%d')
    weekday_index = date_obj.weekday()
    day_name = weekday_mapping[weekday_index]
    print(day_name)