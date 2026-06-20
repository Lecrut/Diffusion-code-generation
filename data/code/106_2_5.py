import datetime

def year_difference(date1, date2):
    return abs(date1.year - date2.year)

if __name__ == '__main__':
    date1 = datetime.datetime(2020, 5, 15)
    date2 = datetime.datetime(2018, 3, 20)
    print(year_difference(date1, date2))