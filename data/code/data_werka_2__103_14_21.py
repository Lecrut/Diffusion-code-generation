from datetime import datetime

def get_elapsed_time_today():
    now = datetime.now()
    seconds_since_midnight = now.hour * 3600 + now.minute * 60 + now.second
    hours = seconds_since_midnight // 3600
    remainder = seconds_since_midnight % 3600
    minutes = remainder // 60
    seconds = remainder % 60
    return f"{hours:02d}:{minutes:02d}:{seconds:02d}"

if __name__ == '__main__':
    print(get_elapsed_time_today())