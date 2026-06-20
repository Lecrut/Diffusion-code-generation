from datetime import datetime

def elapsed_minutes_since_midnight(dt):
    return (dt - dt.replace(hour=0, minute=0, second=0, microsecond=0)).total_seconds() / 60

if __name__ == '__main__':
    sample_dt = datetime(2023, 10, 5, 14, 30)
    print(int(elapsed_minutes_since_midnight(sample_dt)))