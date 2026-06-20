import time

def calculate_year_difference(timestamp1, timestamp2):
    date1 = time.localtime(timestamp1)
    date2 = time.localtime(timestamp2)
    year1, _, _ = date1
    year2, _, _ = date2
    return abs(year1 - year2)
if __name__ == '__main__':
    sample_timestamp1 = 1633075200
    sample_timestamp2 = 1640995200
    print(calculate_year_difference(sample_timestamp1, sample_timestamp2))