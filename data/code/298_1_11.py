from datetime import datetime
TIME_FORMAT = '%H:%M'

def calculate_time_difference(time1_str, time2_str):
    time1 = datetime.strptime(time1_str, TIME_FORMAT)
    time2 = datetime.strptime(time2_str, TIME_FORMAT)
    tdelta = abs(time2 - time1)
    return tdelta.total_seconds()
if __name__ == '__main__':
    time1 = '14:30'
    time2 = '16:45'
    difference = calculate_time_difference(time1, time2)
    print(int(difference))