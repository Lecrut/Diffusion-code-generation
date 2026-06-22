import datetime

def get_weekday(date_str):
    date_obj = datetime.date.fromisoformat(date_str)
    return date_obj.weekday()

if __name__ == '__main__':
    result = get_weekday('2024-07-04')
    print(result)