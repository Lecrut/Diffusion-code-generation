import datetime

def compute_weekday(date_str):
    date_obj = datetime.date.fromisoformat(date_str)
    return date_obj.weekday()

if __name__ == '__main__':
    result = compute_weekday('2024-07-04')
    print(result)