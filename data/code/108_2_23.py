import time

def extract_day_component(time_struct):
    return time_struct.tm_mday

def get_current_day():
    now = time.localtime()
    return extract_day_component(now)

if __name__ == '__main__':
    current_day = get_current_day()
    print(current_day)
    sample_time = time.strptime("2024-01-15 12:00:00", "%Y-%m-%d %H:%M:%S")
    sample_day = extract_day_component(sample_time)
    print(sample_day)