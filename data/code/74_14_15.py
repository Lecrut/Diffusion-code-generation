import datetime
DAY_FORMAT = '%A'

def get_current_day_of_week():
    return datetime.datetime.now().strftime(DAY_FORMAT)
if __name__ == '__main__':
    print(get_current_day_of_week())