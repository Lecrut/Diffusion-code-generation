from datetime import datetime

def elapsed_minutes_since_midnight(dt):
    return (dt.hour * 60) + dt.minute

if __name__ == '__main__':
    sample_dt = datetime(2023, 10, 5, 14, 30)
    print(elapsed_minutes_since_midnight(sample_dt))