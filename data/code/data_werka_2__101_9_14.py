import datetime

def get_weekday(date_str):
    parsed_date = datetime.datetime.strptime(date_str, "%Y-%m-%d")
    return parsed_date.strftime("%A").upper()

if __name__ == '__main__':
    target_date = "2023-11-11"
    day_name = get_weekday(target_date)
    print(day_name)