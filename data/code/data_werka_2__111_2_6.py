import datetime

def get_day_of_week(date_obj):
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    return days[date_obj.weekday()]

if __name__ == '__main__':
    target_date = datetime.date(2024, 2, 29)
    result = get_day_of_week(target_date)
    print(result)