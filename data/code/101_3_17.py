import datetime

if __name__ == '__main__':
    weekday = datetime.datetime.strptime('2023-12-25', '%Y-%m-%d').strftime('%A')
    print(weekday)