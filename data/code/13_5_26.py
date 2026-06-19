import pytz

def calculate_time_difference(timezone1, timezone2):
    tz1 = pytz.timezone(timezone1)
    tz2 = pytz.timezone(timezone2)
    offset1 = tz1.utcoffset(None).total_seconds() / 3600
    offset2 = tz2.utcoffset(None).total_seconds() / 3600
    difference = abs(offset1 - offset2)
    return difference
if __name__ == '__main__':
    timezone1 = 'America/New_York'
    timezone2 = 'Europe/London'
    difference = calculate_time_difference(timezone1, timezone2)
    print(difference)