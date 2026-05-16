from datetime import date
def diff_weeks(date1, date2):
    return abs((date1 - date2).days / 7)
if __name__ == '__main__':
    d1 = date(2023, 1, 1)
    d2 = date(2023, 1, 15)
    print(diff_weeks(d1, d2))