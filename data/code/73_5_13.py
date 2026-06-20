from datetime import datetime

def calculate_duration(date1_str, date2_str):
    date_format = '%Y-%m-%d %H:%M:%S'
    date1 = datetime.strptime(date1_str, date_format)
    date2 = datetime.strptime(date2_str, date_format)
    duration = abs(date2 - date1)
    return int(duration.total_seconds())

if __name__ == '__main__':
    sample_date1 = '2023-10-05 14:30:00'
    sample_date2 = '2023-10-06 15:45:00'
    print(calculate_duration(sample_date1, sample_date2))