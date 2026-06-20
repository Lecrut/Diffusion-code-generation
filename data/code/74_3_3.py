from datetime import datetime

if __name__ == '__main__':
    today = datetime.now()
    day_of_week = today.strftime('%A')
    print(day_of_week)