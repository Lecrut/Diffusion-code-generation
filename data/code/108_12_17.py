from datetime import datetime

def extract_day(timestamp):
    return int(datetime.fromisoformat(timestamp).day)

if __name__ == '__main__':
    timestamp = '2024-07-04T12:00:00'
    print(extract_day(timestamp))