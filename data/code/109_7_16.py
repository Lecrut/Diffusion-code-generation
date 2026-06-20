import datetime

def seconds_remaining_in_month():
    now = datetime.datetime.now()
    end_of_month = datetime.date(now.year, now.month + 1, 1) - datetime.timedelta(days=1)
    return (end_of_month - now).total_seconds()

if __name__ == '__main__':
    print(seconds_remaining_in_month())