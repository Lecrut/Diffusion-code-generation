from datetime import datetime

def timestamp_to_human_readable(timestamp):
    dt_object = datetime.fromtimestamp(timestamp)
    formatted_date = dt_object.strftime('%d-%b-%Y %H:%M:%S')
    return formatted_date

if __name__ == '__main__':
    sample_timestamp = 1633072800
    human_readable_date = timestamp_to_human_readable(sample_timestamp)
    print(human_readable_date)