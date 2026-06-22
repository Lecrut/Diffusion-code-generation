import datetime

def get_day_of_week(date_string):
    date_obj = datetime.datetime.strptime(date_string, "%Y-%m-%d")
    return date_obj.strftime("%A").upper()

if __name__ == '__main__':
    date_str = '2023-11-11'
    result = get_day_of_week(date_str)
    print(result)