import datetime

def get_day_of_week(year, month, day):
    try:
        date_obj = datetime.datetime(year, month, day)
        return date_obj.strftime("%A")
    except ValueError as e:
        raise ValueError(f"Invalid date: {e}")

if __name__ == '__main__':
    sample_date = (2024, 1, 1)
    print(get_day_of_week(*sample_date))