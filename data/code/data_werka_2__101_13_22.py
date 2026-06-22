import datetime

def get_upper_weekday(year, month, day):
    target_date = datetime.date(year, month, day)
    weekday_index = target_date.weekday()
    weekday_names = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    return weekday_names[weekday_index].upper()

if __name__ == '__main__':
    year = 2024
    month = 7
    day = 4
    print(get_upper_weekday(year, month, day))