from datetime import datetime
def calculate_time_diff(date_string1, date_string2):
    dt1 = datetime.fromisoformat(date_string1)
    dt2 = datetime.fromisoformat(date_string2)
    return dt2 - dt1
if __name__ == '__main__':
    date1 = "2023-01-01T10:00:00"
    date2 = "2023-01-05T15:30:00"
    diff = calculate_time_diff(date1, date2)
    print(diff)