import datetime

def is_weekday(date_str):
    date_format = "%Y%m%d"
    date_obj = datetime.datetime.strptime(date_str, date_format)
    return date_obj.weekday() < 5

if __name__ == '__main__':
    sample_dates = ["20231031", "20231101", "20231102", "20231103"]
    results = {date: is_weekday(date) for date in sample_dates}
    print(results)