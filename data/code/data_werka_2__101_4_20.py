import datetime

def get_day_of_week(date_string: str) -> int:
    date_obj = datetime.datetime.strptime(date_string, "%Y-%m-%d")
    return date_obj.weekday()

if __name__ == '__main__':
    sample_date = "2023-10-23"
    result = get_day_of_week(sample_date)
    print(result)