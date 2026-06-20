from datetime import timedelta
WEEKS_PER_DAY = 1 / 7

def weeks_difference(date1, date2):
    delta_days = abs((date2 - date1).days)
    return int(delta_days * WEEKS_PER_DAY)
if __name__ == '__main__':
    d1 = timedelta(days=30)
    d2 = timedelta(days=6)
    print(weeks_difference(d1, d2))