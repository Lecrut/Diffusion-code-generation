import datetime

def get_current_day_of_week():
    current_date = datetime.datetime.now()
    if isinstance(current_date, datetime.datetime):
        return current_date.strftime("%A")
    else:
        raise TypeError("Expected datetime object, got {}".format(type(current_date)))

if __name__ == '__main__':
    print(get_current_day_of_week())