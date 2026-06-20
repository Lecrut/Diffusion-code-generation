from datetime import datetime

def day_of_week(year, month, day):
    return datetime(year, month, day).strftime('%A')

if __name__ == '__main__':
    print(day_of_week(2025, 3, 15))