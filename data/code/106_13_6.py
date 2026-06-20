from datetime import datetime

def years_difference(timestamp1, timestamp2):
    date1 = datetime.fromtimestamp(timestamp1)
    date2 = datetime.fromtimestamp(timestamp2)
    return abs(date1.year - date2.year)
if __name__ == '__main__':
    sample_timestamp1 = 1633072800
    sample_timestamp2 = 1546300800
    print(years_difference(sample_timestamp1, sample_timestamp2))