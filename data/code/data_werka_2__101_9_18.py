import datetime

def get_weekday(date_str):
    parsed = datetime.datetime.strptime(date_str, "%Y-%m-%d")
    return parsed.strftime("%A").upper()

if __name__ == '__main__':
    date_to_check = "2023-11-11"
    print(get_weekday(date_to_check))