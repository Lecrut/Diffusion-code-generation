import datetime

def get_weekday(date_obj):
    return date_obj.strftime('%A').upper()

if __name__ == '__main__':
    target_date = datetime.date(2024, 7, 4)
    result = get_weekday(target_date)
    print(result)