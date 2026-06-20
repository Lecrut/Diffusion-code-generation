from datetime import datetime

if __name__ == '__main__':
    weekday = datetime.strptime('2023-12-25', '%Y-%m-%d').weekday()
    print(weekday)