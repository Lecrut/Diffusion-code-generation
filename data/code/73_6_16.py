import datetime

def calculate_time_difference(dt1, dt2):
    difference = dt2 - dt1
    return difference

if __name__ == '__main__':
    time_values = {
        'time1': datetime.datetime(2023, 1, 1, 10, 0, 0),
        'time2': datetime.datetime(2022, 1, 1, 10, 0, 0),
        'time3': datetime.datetime(2023, 1, 1, 11, 0, 0)
    }
    
    diff1 = calculate_time_difference(time_values['time1'], time_values['time2'])
    print(f"Difference between time1 and time2: {diff1}")
    
    diff2 = calculate_time_difference(time_values['time3'], time_values['time1'])
    print(f"Difference between time1 and time3: {diff2}")