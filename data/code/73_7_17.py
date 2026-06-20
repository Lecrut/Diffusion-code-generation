import datetime

def date_difference(date1_str, date2_str):
    date_format = "%Y-%m-%d %H:%M:%S"
    date1 = datetime.datetime.strptime(date1_str, date_format)
    date2 = datetime.datetime.strptime(date2_str, date_format)
    return abs((date2 - date1).total_seconds() / 60)

if __name__ == '__main__':
    sample_date_a = "2023-10-29 10:00:00"
    sample_date_b = "2023-11-02 14:30:00"
    difference = date_difference(sample_date_a, sample_date_b)
    print(difference)