from datetime import datetime

def fraction_of_month_remaining():
    now = datetime.now()
    days_in_month = (now.replace(day=28) + timedelta(days=4)).day
    days_passed = now.day - 1
    return days_passed / days_in_month

if __name__ == '__main__':
    print(fraction_of_month_remaining())