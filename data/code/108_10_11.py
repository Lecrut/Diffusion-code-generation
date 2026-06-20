import datetime

def get_day_of_week():
    date_obj = datetime.datetime(2024, 1, 1)
    return date_obj.strftime("%A")

if __name__ == '__main__':
    print(get_day_of_week())