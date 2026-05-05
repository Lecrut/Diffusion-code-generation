import datetime
if __name__ == '__main__':
    now = datetime.datetime.now()
    day_of_week = now.strftime("%A")
    print(day_of_week)