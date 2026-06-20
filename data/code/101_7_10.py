import datetime

def get_weekday(date_str):
    date_obj = datetime.date.fromisoformat(date_str)
    return date_obj.weekday()

if __name__ == '__main__':
    sample_date = '2024-07-04'
    weekday_index = get_weekday(sample_date)
    print(weekday_index)