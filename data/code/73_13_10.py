import datetime

def calculate_time_difference(date_str1, date_str2):
    try:
        dt1 = datetime.datetime.fromisoformat(date_str1)
        dt2 = datetime.datetime.fromisoformat(date_str2)
        time_difference = abs(dt1 - dt2)
        return int(time_difference.total_seconds())
    except ValueError:
        return -1

if __name__ == '__main__':
    date1_input = "2023-10-27T10:00:00Z"
    date2_input = "2023-10-27T10:05:30Z"
    result = calculate_time_difference(date1_input, date2_input)
    print(result)