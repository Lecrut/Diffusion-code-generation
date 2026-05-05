from datetime import datetime
if __name__ == '__main__':
    date1 = datetime(2023, 1, 1)
    date2 = datetime(2023, 1, 10)
    difference = abs((date2 - date1).days)
    print(difference)