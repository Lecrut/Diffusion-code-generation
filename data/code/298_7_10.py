from datetime import datetime

def calculate_duration(start_time_str, end_time_str):
    start_time = datetime.strptime(start_time_str, '%H:%M')
    end_time = datetime.strptime(end_time_str, '%H:%M')
    
    duration = (end_time - start_time).seconds
    
    return duration

if __name__ == '__main__':
    sample_duration = calculate_duration('11:30', '14:15')
    print(sample_duration)