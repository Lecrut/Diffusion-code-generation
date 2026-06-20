import datetime

def month_diff(timestamp1, timestamp2):
    date1 = datetime.datetime.fromtimestamp(timestamp1)
    date2 = datetime.datetime.fromtimestamp(timestamp2)
    return (date2.year - date1.year) * 12 + (date2.month - date1.month)
if __name__ == '__main__':
    print(month_diff(1633075200, 1664611200))