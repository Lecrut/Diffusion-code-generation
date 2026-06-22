import datetime

DATE_FORMAT = "%Y-%m-%d"
DATE_STRING = "2023-11-11"

def get_weekday(date_str):
    parsed_date = datetime.datetime.strptime(date_str, DATE_FORMAT)
    return parsed_date.strftime("%A").upper()

if __name__ == '__main__':
    print(get_weekday(DATE_STRING))