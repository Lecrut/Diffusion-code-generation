from datetime import datetime

def extract_day_from_timestamp(timestamp):
    dt = datetime.strptime(timestamp, '%Y-%m-%dT%H:%M:%S')
    return dt.day

if __name__ == '__main__':
    timestamp = '2024-07-04T12:00:00'
    day = extract_day_from_timestamp(timestamp)
    print(day)