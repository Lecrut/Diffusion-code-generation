import time
SECONDS_PER_YEAR = 31536000

def calculate_year_difference(timestamp1, timestamp2):
    return abs((timestamp1 - timestamp2) // SECONDS_PER_YEAR)
if __name__ == '__main__':
    sample_timestamp1 = 1633075200
    sample_timestamp2 = 1609459200
    print(calculate_year_difference(sample_timestamp1, sample_timestamp2))