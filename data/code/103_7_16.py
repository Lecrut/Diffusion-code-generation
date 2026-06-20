import datetime

def time_elapsed_since_midnight():
    now = datetime.datetime.now()
    midnight = datetime.datetime(now.year, now.month, now.day)
    elapsed_time = now - midnight
    return elapsed_time

if __name__ == '__main__':
    sample_result = time_elapsed_since_midnight()
    print(f"Time elapsed since midnight: {sample_result}")