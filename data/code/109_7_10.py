import datetime

def calculate_days_remaining():
    today = datetime.date.today()
    end_of_month = (today.replace(day=28) + datetime.timedelta(days=4)).replace(day=1) - datetime.timedelta(days=1)
    days_remaining = (end_of_month - today).days + 1
    return days_remaining

if __name__ == '__main__':
    result = calculate_days_remaining()
    print(result)