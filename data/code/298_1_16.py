from datetime import datetime
TIME_FORMAT = '%H:%M'
START_TIME = '14:30'
END_TIME = '16:45'

def calculate_time_difference(time1_str, time2_str):
    start_time = datetime.strptime(time1_str, TIME_FORMAT)
    end_time = datetime.strptime(time2_str, TIME_FORMAT)
    return (end_time - start_time).seconds
if __name__ == '__main__':
    print(calculate_time_difference(START_TIME, END_TIME))