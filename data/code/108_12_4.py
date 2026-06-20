from datetime import datetime

def extract_day(timestamp):
    dt = datetime.fromisoformat(timestamp)
    return dt.day

if __name__ == '__main__':
    timestamp = '2024-07-04T12:00:00'
    print(extract_day(timestamp))