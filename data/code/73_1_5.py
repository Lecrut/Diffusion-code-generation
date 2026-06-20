from datetime import datetime, timedelta

def calculate_time_diff(date_str1, date_str2):
    date_format = "%Y-%m-%dT%H:%M:%S%z"
    dt1 = datetime.strptime(date_str1, date_format)
    dt2 = datetime.strptime(date_str2, date_format)
    return abs(dt1 - dt2)

if __name__ == '__main__':
    sample_date1 = "2023-04-01T12:00:00+00:00"
    sample_date2 = "2023-04-01T14:30:00+00:00"
    print(calculate_time_diff(sample_date1, sample_date2))