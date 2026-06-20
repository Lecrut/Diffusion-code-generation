import datetime

def get_weekday(date_str):
    try:
        date_obj = datetime.date.fromisoformat(date_str)
        return date_obj.weekday()
    except ValueError:
        return None

if __name__ == '__main__':
    sample_date = '2024-07-04'
    weekday = get_weekday(sample_date)
    print(weekday)