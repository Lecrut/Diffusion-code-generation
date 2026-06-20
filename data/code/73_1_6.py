from datetime import datetime, timedelta

def calculate_time_diff(date_str1, date_str2):
    date_format = "%Y-%m-%dT%H:%M:%S%z"
    date1 = datetime.strptime(date_str1, date_format)
    date2 = datetime.strptime(date_str2, date_format)
    return abs(date2 - date1)

if __name__ == '__main__':
    sample_date1 = "2023-10-01T12:00:00+0000"
    sample_date2 = "2023-10-02T14:30:00+0000"
    print(calculate_time_diff(sample_date1, sample_date2))