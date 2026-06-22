import datetime

def get_day_name_upper(date_string):
    parsed_date = datetime.datetime.strptime(date_string, "%Y-%m-%d")
    weekday_name = parsed_date.strftime("%A")
    return weekday_name.upper()

if __name__ == '__main__':
    sample_date = "2023-11-11"
    output = get_day_name_upper(sample_date)
    print(output)