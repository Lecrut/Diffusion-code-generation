from datetime import datetime, timedelta
ISO_FORMAT = '%Y-%m-%dT%H:%M:%S'

def calculate_time_diff(date_string1, date_string2):
    dt1 = datetime.strptime(date_string1, ISO_FORMAT)
    dt2 = datetime.strptime(date_string2, ISO_FORMAT)
    return dt2 - dt1
if __name__ == '__main__':
    sample_date1 = '2023-01-01T10:00:00'
    sample_date2 = '2023-01-05T14:30:00'
    diff = calculate_time_diff(sample_date1, sample_date2)
    print(diff)