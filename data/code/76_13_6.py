from datetime import datetime

def get_date_difference(date1, date2):
    return abs((date2 - date1).days)

if __name__ == '__main__':
    sample_date1 = datetime(2023, 1, 1)
    sample_date2 = datetime(2023, 1, 10)
    difference = get_date_difference(sample_date1, sample_date2)
    print(difference)