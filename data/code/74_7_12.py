import datetime
DAY_NAMES = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

def get_current_day_of_week():
    current_date = datetime.datetime.now()
    return DAY_NAMES[current_date.weekday()]
if __name__ == '__main__':
    print(get_current_day_of_week())