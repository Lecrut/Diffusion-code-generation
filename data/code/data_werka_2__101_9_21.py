import datetime

def compute_weekday(date_value):
    parsed_date = datetime.datetime.strptime(date_value, "%Y-%m-%d")
    weekday_index = parsed_date.weekday()
    full_name = parsed_date.strftime("%A")
    return full_name.upper()

if __name__ == '__main__':
    sample_date = "2023-11-11"
    day_result = compute_weekday(sample_date)
    print(day_result)