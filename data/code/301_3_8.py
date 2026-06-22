from datetime import datetime

def timestamp_to_human_readable(timestamp):
    try:
        dt_object = datetime.fromtimestamp(timestamp)
        formatted_date = dt_object.strftime('%d-%b-%Y %H:%M:%S')
        return formatted_date
    except (ValueError, OSError) as e:
        raise ValueError(f"Invalid timestamp: {e}")

if __name__ == '__main__':
    sample_timestamps = [1633072800, 1672531200]
    for timestamp in sample_timestamps:
        print(timestamp_to_human_readable(timestamp))