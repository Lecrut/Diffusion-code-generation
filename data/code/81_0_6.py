from datetime import datetime

def time_elapsed(start_time_str, end_time_str):
    start_time = datetime.strptime(start_time_str, "%H:%M")
    end_time = datetime.strptime(end_time_str, "%H:%M")
    
    if end_time < start_time:
        end_time += timedelta(days=1)
    
    elapsed_time = (end_time - start_time).seconds // 3600
    return elapsed_time

if __name__ == '__main__':
    print(time_elapsed("23:59", "00:01"))