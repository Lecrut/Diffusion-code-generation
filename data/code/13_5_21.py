import datetime

def calculate_time_difference(timezone1, timezone2):
    tz1 = datetime.timezone(datetime.timedelta(hours=int(timezone1.split(':')[0])))
    tz2 = datetime.timezone(datetime.timedelta(hours=int(timezone2.split(':')[0])))
    difference = (tz2.utcoffset(None) - tz1.utcoffset(None)).total_seconds() / 3600
    return abs(difference)
if __name__ == '__main__':
    timezone1 = 'UTC:0'
    timezone2 = 'EST:-5'
    difference = calculate_time_difference(timezone1, timezone2)
    print(difference)