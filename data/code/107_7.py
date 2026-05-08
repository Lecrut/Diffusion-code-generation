import datetime
def date_to_timestamp(date_string):
    dt_object = datetime.datetime.strptime(date_string, '%Y-%m-%d')
    return int(dt_object.timestamp())
if __name__ == '__main__':
    date_str1 = "2023-10-27"
    timestamp1 = date_to_timestamp(date_str1)
    print(f"{date_str1}: {timestamp1}")
    date_str2 = "1999-01-01"
    timestamp2 = date_to_timestamp(date_str2)
    print(f"{date_str2}: {timestamp2}")