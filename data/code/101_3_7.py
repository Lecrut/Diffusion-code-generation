from datetime import datetime

weekday_mapping = {
    0: 'Monday', 1: 'Tuesday', 2: 'Wednesday',
    3: 'Thursday', 4: 'Friday', 5: 'Saturday', 6: 'Sunday'
}

def get_weekday(date_string):
    date_obj = datetime.strptime(date_string, '%Y-%m-%d')
    weekday_index = date_obj.weekday()
    return weekday_mapping[weekday_index]

if __name__ == '__main__':
    sample_date = '2023-12-25'
    day_name = get_weekday(sample_date)
    print(day_name)