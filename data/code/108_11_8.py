import datetime
TARGET_DATE = datetime.date(2023, 3, 15)

def get_day_of_month(date_obj):
    try:
        return date_obj.day
    except AttributeError:
        return None
if __name__ == '__main__':
    target_day = get_day_of_month(TARGET_DATE)
    print(f'Day of month for {TARGET_DATE}: {target_day}')