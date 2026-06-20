from datetime import datetime

def timestamp_to_date(timestamp):
    dt_object = datetime.fromtimestamp(timestamp)
    return f"{dt_object.year:04d}/{dt_object.month:02d}/{dt_object.day:02d}"

if __name__ == '__main__':
    sample_timestamp = 1633075200
    formatted_date = timestamp_to_date(sample_timestamp)
    print(formatted_date)