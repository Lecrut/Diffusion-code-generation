from datetime import datetime
def calculate_time_difference(date1, date2):
    difference = abs(date1 - date2)
    return difference
if __name__ == '__main__':
    time1 = datetime(2023, 1, 1, 10, 0, 0)
    time2 = datetime(2023, 1, 5, 14, 30, 0)
    diff = calculate_time_difference(time1, time2)
    print(diff)