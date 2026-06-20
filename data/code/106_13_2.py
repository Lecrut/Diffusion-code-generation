import datetime

def calculate_year_difference(timestamp1, timestamp2):
    date1 = datetime.datetime.fromtimestamp(timestamp1)
    date2 = datetime.datetime.fromtimestamp(timestamp2)
    return abs(date1.year - date2.year)
if __name__ == '__main__':
    print(calculate_year_difference(1609459200, 1672531200))