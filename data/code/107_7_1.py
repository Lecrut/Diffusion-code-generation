import datetime
def date_to_timestamp(date_string):
    dt_object = datetime.datetime.strptime(date_string, "%Y-%m-%d")
    return int(dt_object.timestamp())
if __name__ == '__main__':
    date_str_1 = "2023-10-27"
    timestamp_1 = date_to_timestamp(date_str_1)
    print(f"{date_str_1}: {timestamp_1}")
    date_str_2 = "1999-01-01"
    timestamp_2 = date_to_timestamp(date_str_2)
    print(f"{date_str_2}: {timestamp_2}")