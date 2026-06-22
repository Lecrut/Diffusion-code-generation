import datetime

def get_day_of_week(date_str):
    date_obj = datetime.datetime.strptime(date_str, "%Y-%m-%d")
    return date_obj.strftime("%A")

if __name__ == '__main__':
    date_string = "2023-10-05"
    day_name = get_day_of_week(date_string)
    print(day_name)