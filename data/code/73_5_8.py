from datetime import datetime

def calculate_duration(date1_str, date2_str):
    date_format = '%Y-%m-%d %H:%M:%S'
    date1 = datetime.strptime(date1_str, date_format)
    date2 = datetime.strptime(date2_str, date_format)
    time_difference = abs(date2 - date1)
    return time_difference

if __name__ == '__main__':
    date1 = '2023-10-01 12:00:00'
    date2 = '2023-10-02 14:30:00'
    duration = calculate_duration(date1, date2)
    print(f"Time difference: {duration}")