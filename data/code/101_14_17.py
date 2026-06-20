from datetime import datetime

def day_of_week(year, month, day):
    date = datetime(year, month, day)
    return date.strftime("%A")

if __name__ == '__main__':
    print(day_of_week(2025, 3, 15))