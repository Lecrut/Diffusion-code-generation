import datetime

def get_current_day():
    return datetime.datetime.now().strftime('%A')

if __name__ == '__main__':
    print(get_current_day())