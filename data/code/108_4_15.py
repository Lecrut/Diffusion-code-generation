import calendar

def get_day_of_week(year=2023, month=10, day=5):
    return calendar.monthrange(year, month)[1]

if __name__ == '__main__':
    print(get_day_of_week())