from datetime import datetime

def date_difference(date_str1, date_str2):
    format_str = "%Y-%m-%d %H:%M:%S"
    dt1 = datetime.strptime(date_str1, format_str)
    dt2 = datetime.strptime(date_str2, format_str)
    return abs(dt2 - dt1)

if __name__ == '__main__':
    sample_date1 = "2023-10-01 12:00:00"
    sample_date2 = "2023-10-05 14:30:00"
    print(date_difference(sample_date1, sample_date2))