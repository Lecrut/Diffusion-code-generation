from datetime import datetime

def timestamp_to_human_readable(timestamp):
    dt_object = datetime.fromtimestamp(timestamp)
    formatted_date = dt_object.strftime('%d-%b-%Y %H:%M:%S')
    return formatted_date

if __name__ == '__main__':
    sample_timestamp = 1609459200
    print(timestamp_to_human_readable(sample_timestamp))