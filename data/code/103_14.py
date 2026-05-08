import datetime
def get_total_minutes_today():
    now = datetime.datetime.now()
    start_of_day = now.replace(hour=0, minute=0, second=0, microsecond=0)
    time_difference = now - start_of_day
    total_minutes = time_difference.total_seconds() // 60
    return int(total_minutes)
if __name__ == '__main__':
    print(get_total_minutes_today())