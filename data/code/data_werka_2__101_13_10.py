import datetime

def get_weekday_for_date(year, month, day):
    try:
        date_obj = datetime.date(year, month, day)
    except ValueError:
        raise ValueError("Invalid date provided")
    return date_obj.strftime("%A").upper()

if __name__ == '__main__':
    result = get_weekday_for_date(2024, 7, 4)
    print(result)