import datetime

def date_difference(date1_str, date2_str):
    date_format = "%Y-%m-%d %H:%M:%S"
    date1 = datetime.datetime.strptime(date1_str, date_format)
    date2 = datetime.datetime.strptime(date2_str, date_format)
    difference = abs((date2 - date1).total_seconds()) / 60
    return int(difference)

if __name__ == '__main__':
    sample_dates = {
        "start": "2023-10-29 10:00:00",
        "end": "2023-11-02 14:30:00"
    }
    difference_minutes = date_difference(sample_dates["start"], sample_dates["end"])
    print(difference_minutes)