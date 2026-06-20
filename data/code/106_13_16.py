from datetime import datetime
SECONDS_IN_YEAR = 31536000

def calculate_year_difference(timestamp1, timestamp2):
    date1 = datetime.fromtimestamp(timestamp1)
    date2 = datetime.fromtimestamp(timestamp2)
    return abs((date1 - date2).days // SECONDS_IN_YEAR)
if __name__ == '__main__':
    sample_timestamp1 = 1633075200
    sample_timestamp2 = 1609459200
    print(calculate_year_difference(sample_timestamp1, sample_timestamp2))