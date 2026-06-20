from datetime import datetime

def calculate_year_difference(timestamp1, timestamp2):
    date1 = datetime.fromtimestamp(timestamp1)
    date2 = datetime.fromtimestamp(timestamp2)
    return abs(date1.year - date2.year)
if __name__ == '__main__':
    sample_timestamp1 = 1609459200
    sample_timestamp2 = 1672531200
    print(calculate_year_difference(sample_timestamp1, sample_timestamp2))