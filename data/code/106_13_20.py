import datetime
SECONDS_PER_YEAR = 31536000

def calculate_year_difference(timestamp1, timestamp2):
    date1 = datetime.datetime.fromtimestamp(timestamp1)
    date2 = datetime.datetime.fromtimestamp(timestamp2)
    return abs(date1.year - date2.year)
if __name__ == '__main__':
    sample_timestamp1 = 1633075200
    sample_timestamp2 = 1609459200
    print(calculate_year_difference(sample_timestamp1, sample_timestamp2))