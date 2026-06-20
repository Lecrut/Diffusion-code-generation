from datetime import date

def years_difference(date1, date2):
    return abs((date2 - date1).days // 365)

if __name__ == '__main__':
    print(years_difference(date(2000, 1, 1), date(2023, 4, 1)))